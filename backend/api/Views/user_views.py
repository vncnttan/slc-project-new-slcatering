from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import permissions
from api.models import User
from api.serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
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
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

@swagger_auto_schema(
    method='get',
    security=[{'Bearer': []}],
    operation_description=(
        "Retrieve user data. "
        "If the 'all' parameter is provided and set to true, all users are retrieved. "
        "Otherwise, retrieves specific user data."
    ),
    manual_parameters=[
        openapi.Parameter(
            name='all',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_BOOLEAN,
            description="Get all users parameter",
            required=False
        ),
    ],
    responses={
        200:"Succesfull response",
        500: "Unexpected error"
    }
)
@swagger_auto_schema(
    method='delete',
    security=[{'Bearer': []}],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'user_id' : openapi.Schema(type=openapi.TYPE_STRING, description="User id to be deleted")
        },
        required=['user_id']
        
    ),
    responses={
        200:"Succesfully response",
        406 : "You cannot delete your own account",
        404: "User does not exist",
        500 : "Unexpected error"
    }
)
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


@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username' : openapi.Schema(type=openapi.TYPE_STRING, description="Fill in with username"),
            'password' : openapi.Schema(type=openapi.TYPE_STRING, description="Fill in with password"),
            'email': openapi.Schema(type=openapi.TYPE_STRING, description="Fill in with email"),
            'confirm_password' : openapi.Schema(type=openapi.TYPE_STRING, description="Fill in with confirm password"), 
        },
        required=['username', 'password', "email", "confirm_password"]
    ),
    responses={
        201: "Succesfull created user account",
        400: "Validation error / SMTP Error",
        500: "Unexpected error"
    }
)
@api_view(['POST'])
def register(request):
    # On Progress: Change to LoginView using Messier API
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


@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'enc_token': openapi.Schema(type=openapi.TYPE_STRING, description="Encoded user token")
        },
        required=['enc_token']
    ),
    responses={
        200: "Succesfull response",
        406: "User already activated",
        500: "Unexpected error"
    }
)
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
        return JsonResponse({'message':'Oops something went wrong', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username' : openapi.Schema(type=openapi.TYPE_STRING, description="Fill in with username"),
            'password' : openapi.Schema(type=openapi.TYPE_STRING, description="Fill in with password")
        },
        required=['username', 'password']
    ),
    responses={
        200: "Succesfull response",
        400: "Invalid username / password",
        500: "Unexpected error"
    }
)
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
        return JsonResponse({"message" : "Oops ! Something went wrong", "error" : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def get_user(request):
    try:
        user_id = request.user_id
        user = User.objects.get(id=str(user_id))
        ser_data = UserSerializer(user).data
        # ser_data.pop('password')
        return JsonResponse(ser_data, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({"message" : "Oops something went wrong !", "error" : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
        return JsonResponse({"message": "Oops something went wrong", "error" : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username' : openapi.Schema(type=openapi.TYPE_STRING, description="Fill in with username"),
            'password' : openapi.Schema(type=openapi.TYPE_STRING, description="Fill in with password"),
            'email': openapi.Schema(type=openapi.TYPE_STRING, description="Fill in with email"),
            'confirm_password' : openapi.Schema(type=openapi.TYPE_STRING, description="Fill in with confirm password"), 
        },
        required=['username', 'password', "email", "confirm_password"]
    ),
    responses={
        201: "Succesfull created seller account",
        400: "Validation error / SMTP Error",
        500: "Unexpected error"
    }
)
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
        return JsonResponse({"message" : "Oops something went wrong", "error" : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)