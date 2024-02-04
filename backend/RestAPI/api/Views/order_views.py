from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
import jwt
from django.conf import settings
from django.http.response import JsonResponse
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from api.models import User,Order
from api.serializers import OrderViewSerializer
from api.services import order_services, user_services
from django.contrib.auth.hashers import make_password, check_password

@api_view(["POST", "GET"])
def order(request):
    if request.method == "POST":
        return create_order(request)
    elif request.method == "GET":
        return get_orders(request)

def get_orders(request):
    try:
        id = request.GET.get('id')
        if request.GET.get('id'):
            order = Order.objects.filter(catering = id)
            order_serializer = OrderViewSerializer(order, many=True).data
            return JsonResponse(order_serializer, status=status.HTTP_200_OK, safe=False)
        elif request.user_id:
            order = Order.objects.filter(ordered_by = request.user_id)
            serializer_order = OrderViewSerializer(order, many=True).data
            return JsonResponse(serializer_order, status=status.HTTP_200_OK, safe=False)
    except Exception as e :
        return JsonResponse({"message": "Bad request", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

def create_order(request):
    try:
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        data = JSONParser().parse(request)
        if auth_header:
            try:
                token_type, token = auth_header.split(' ')
                if token_type == "Bearer":
                    token = token.encode('utf-8')
                    decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                    user_id = decoded_token.get('user_id')
                    return order_services.create_order(user_id=user_id,order=data)
            except (InvalidToken, TokenError, User.DoesNotExist):
                return JsonResponse({"message" : "Invalid token !"}, status=status.HTTP_401_UNAUTHORIZED)
            except jwt.ExpiredSignatureError:
                return JsonResponse({"message" : "Token expired !"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        elif data['username'] or data['password']:
            user = user_services.get_spesific_user_by_username(data['username'])
            if user is None:
                return JsonResponse({"message" : "Invalid username/password"}, status=status.HTTP_401_UNAUTHORIZED)
            
            if check_password(data['password'], user.password):
                return order_services.create_order(user.id, data)
            else:
                return JsonResponse({"message" : "Invalid username/password"}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return JsonResponse({"message" : "Bad request", "error" : str(e)}, status=status.HTTP_400_BAD_REQUEST)