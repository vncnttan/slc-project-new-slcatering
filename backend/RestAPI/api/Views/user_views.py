from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from api.models import User
from api.serializers import UserSerializer
from rest_framework.decorators import api_view
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from django.template.loader import render_to_string
import base64
import jwt
from api.services.user_services import get_spesific_user_by_username
from django.http import HttpResponse
from datetime import datetime, timedelta

# Create your views here.

# @api_view(['POST'])
# def login(request):

@api_view(["GET", "DELETE"])
def user(request):
    if request.method == "GET":
        # print(request.GET.get('active'))
        if(request.GET.get('all')):
            
            return get_all_user(request)
        return get_user(request)
    elif request.method == "DELETE":
        # print("DELETE")
        return delete_user(request)

def get_all_user(request):
    users = None
    if(request.GET.get("active") == "True"):
        users = User.objects.filter(is_activated = True)
    elif(request.GET.get("active") == "False"):
        users = User.objects.filter(is_activated = False)
    else:
        users = User.objects.all()
    users_serializer = UserSerializer(users, many=True).data
    return JsonResponse(users_serializer, status=status.HTTP_200_OK, safe=False)


@api_view(['POST'])
def register(request):
    try:
        data = JSONParser().parse(request)
        if data['username'] == "" or data['password'] == '' or data['email'] == "" or data['confirm_password'] == '':
            return JsonResponse({"message":"Please fill in all the fields"}, status=status.HTTP_400_BAD_REQUEST)

        if data['password'] != data['confirm_password']:
            return JsonResponse({"message":"Password is not matched"}, status=status.HTTP_400_BAD_REQUEST)


        data['password'] = make_password(data['password'])
        data['is_activated'] = False
        data['created_at'] = datetime.now()
        data['role'] = 'user'

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            token = jwt.encode({"id":str(user.id), "exp":datetime.now() + timedelta(hours=1)}, settings.SECRET_KEY, algorithm='HS256' )
            link = settings.FRONTEND_HOST + "/activate/"+ base64.urlsafe_b64encode(token.encode('utf-8')).decode('utf-8')
            email_content = render_to_string('activation_email.html', {'activation_link': link})
            send_mail(
                "Activate account",
                "Activate your account." ,
                settings.EMAIL_HOST_USER,
                [data['email']],
                fail_silently=False,
                html_message=email_content
            )
            ser_data = serializer.data
            return JsonResponse(ser_data, status=status.HTTP_201_CREATED)

        errors = serializer.errors
        _ , first_errors = next(iter(errors.items()))
        first_error_message = first_errors[0] if first_errors else "Unknown error"
        return JsonResponse({"message":first_error_message}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e :
        return JsonResponse({"message" : "Bad request", "error" : str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def activate_email(request):
    try:
        data = JSONParser().parse(request)
        enctoken = data['enc_token']
        token = base64.urlsafe_b64decode(enctoken).decode('utf-8')
        token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user = User.objects.get(id=token['id'])
        if(user.is_activated):
            return JsonResponse({'message': 'User already activated'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        user.is_activated = True
        user.save()
        return JsonResponse({'message':'Succesfully activated account'}, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({'message':'Invalid link', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    try:
        data = JSONParser().parse(request)
        user = get_spesific_user_by_username(data['username'])
        if user is None:
            return JsonResponse({'message': 'Invalid username / password'}, status=status.HTTP_400_BAD_REQUEST)
        if check_password(data['password'], user.password):
            token = AccessToken().for_user(user=user)
            # print(token)
            return JsonResponse({'access_token' : str(token), 'message': 'Login Succesfully !'}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'message' : 'Invalid username / password'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return JsonResponse({"message" : "Bad request", "error" : str(e)}, status=status.HTTP_400_BAD_REQUEST)

def get_user(request):
    try:
        user_id = request.user_id
        user = User.objects.get(id=str(user_id))
        ser_data = UserSerializer(user).data
        # ser_data.pop('password')
        return JsonResponse(ser_data, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({"message" : "Bad request", "error" : str(e)}, status=status.HTTP_400_BAD_REQUEST)

def delete_user(request):
    try:
        curr_userid = request.user_id.replace('-', '')
        data = JSONParser().parse(request)
        if(curr_userid == data['user_id'].replace('-', '')):
            return JsonResponse({"message":"You cannot delete your own account"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        user = User.objects.get(id=data["user_id"])
        user_delete_username = user.username
        user.delete()
        return JsonResponse({"message": "Successfully deleted "+user_delete_username}, status=status.HTTP_200_OK)
    except(User.DoesNotExist):
        return JsonResponse({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JsonResponse({"message": "Bad request", "error" : str(e)}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e :
        return JsonResponse({"message" : "Bad request", "error" : str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def seller_register(request):
    try :
        data = JSONParser().parse(request)
        if data['username'] == "" or data['password'] == '' or data['email'] == "" or data['confirm_password'] == '':
            return JsonResponse({"message":"Please fill in all the fields"}, status=status.HTTP_400_BAD_REQUEST)

        if data['password'] != data['confirm_password']:
            return JsonResponse({"message":"Password is not matched"}, status=status.HTTP_400_BAD_REQUEST)


        data['password'] = make_password(data['password'])
        data['is_activated'] = False
        data['created_at'] = datetime.now()
        data['role'] = 'seller'

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            token = jwt.encode({"id":str(user.id), "exp":datetime.now() + timedelta(hours=1)}, settings.SECRET_KEY, algorithm='HS256' )
            link = settings.FRONTEND_HOST + "/activate/"+ base64.urlsafe_b64encode(token.encode('utf-8')).decode('utf-8')
            email_content = render_to_string('activation_email.html', {'activation_link': link})
            send_mail(
                "Activate seller account",
                "Activate your account." ,
                settings.EMAIL_HOST_USER,
                [data['email']],
                fail_silently=False,
                html_message=email_content
            )
            ser_data = serializer.data
            # ser_data.pop('password')
            return JsonResponse(ser_data, status=status.HTTP_201_CREATED)

        errors = serializer.errors
        _ , first_errors = next(iter(errors.items()))
        first_error_message = first_errors[0] if first_errors else "Unknown error"
        return JsonResponse({"message":first_error_message}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e :
        return JsonResponse({"message" : "Bad request", "error" : str(e)}, status=status.HTTP_400_BAD_REQUEST)