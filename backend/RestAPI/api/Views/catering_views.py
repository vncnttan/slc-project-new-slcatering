from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status
from datetime import datetime
from api.serializers import CateringSerializer, CateringViewSerializer
from api.services import user_services, catering_services
from api.models import Catering


@api_view(["GET", "POST", "PATCH"])
def catering(request):
    if request.method == "GET":
        if request.GET.get('active') == "True":
            return get_active_caterings(request)
        elif request.GET.get('active') == "False":
            if request.GET.get('user'):
                return 
            catering = catering_services.get_all_catering_history()
            if catering == None:
                return JsonResponse({"message" : "Catering does not exist"}, status=status.HTTP_404_NOT_FOUND)
            return JsonResponse(catering.data, status=status.HTTP_200_OK, safe=False)
        else:
            catering = catering_services.get_all_caterings()
            if catering == None:
                return JsonResponse({"message" : "Catering does not exist"}, status=status.HTTP_404_NOT_FOUND)
            else:
                return JsonResponse(catering.data, status=status.HTTP_200_OK, safe=False)
    elif request.method == "POST":
        return create_catering(request)
    elif request.method == "PATCH":
        return close_catering(request)


def close_catering(request):
    data = JSONParser().parse(request)
    try:
        catering = Catering.objects.get(id=data['catering_id'])
        if 'catering_id' in data and catering is not None and catering.is_closed is False:
            catering.is_closed = True
            catering.save()
            return JsonResponse({"message": "Succesfully closed catering"}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"message": "Catering not found"}, status=status.HTTP_400_BAD_REQUEST)
    except(Catering.DoesNotExist):
        return JsonResponse({"message":"Catering not found"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e :
        return JsonResponse({"message" : "Bad Request", "error" : str(e) }, status=status.HTTP_400_BAD_REQUEST)

def get_active_caterings(request):
    caterings = catering_services.get_active_caterings()
    if caterings is not None :
        return JsonResponse(caterings.data,safe=False, status=status.HTTP_200_OK)
    else:
        return JsonResponse([], status=status.HTTP_200_OK)


def create_catering(request):
    try :
        data = JSONParser().parse(request)
        if data['title'] == "" or data["price"] == 0:
            return JsonResponse({"message":"Fill in all the fields"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = user_services.get_spesific_user_by_id(request.user_id)
        
        if not user or user.role != 'seller' or not user.is_activated:
            return JsonResponse({"message" : "Your account is not authorized to create a catering"}, status=status.HTTP_401_UNAUTHORIZED)
        
        data["created_at"] = datetime.now()
        data['created_by'] = user.id
        data['is_closed'] = False
        
        serializer = CateringSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else :
            return JsonResponse({'message' : 'Failed to proccess data'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except Exception as e:
        return JsonResponse({"message" : "Bad request", "error" : str(e)}, status=status.HTTP_400_BAD_REQUEST)