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
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(
    method='get',
    operation_description=(
        "Retrive orders. "
        "If there is id in the request parameter, then it will get all order from a catering. "
        "If there is no id in the request parameter, then it will get all order from a current logged in user."
    ),
    manual_parameters=[
        openapi.Parameter(
            name='id',
            in_= openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            description="Get all order from a spesific catering",
            required=False
        ),
    ],
    responses={
        200: "Succesfull response",
        403 : "Access denied",
        500 : "Unexpected error"
    }
)
@swagger_auto_schema(
    method='post',
    operation_description=(
        "Create orders. "
        "Create catering orders for users"
    ),
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "username" : openapi.Schema(type=openapi.TYPE_STRING, description="Username can be used if the user is not logged in"),
            "password" : openapi.Schema(type=openapi.TYPE_STRING, description="Password can be used if the user is not logged in"),
            "catering" : openapi.Schema(type=openapi.TYPE_STRING, description="Catering id used to determine which catering user wants to order"),
            "variant": openapi.Schema(type=openapi.TYPE_STRING, description="Variant catering id used to determine which variant catering user want to order"),
            "notes" : openapi.Schema(type=openapi.TYPE_STRING, description="User notes for the seller")
        },
        required=['catering', 'variant', 'notes']
        
    ),
    responses={
        200 : "Succesfull response",
        400 : "Bad request",
        402 : "User has too much debt",
        403 : "Authentication needed",
        406 : "Out of stock",
        500 : "Unexpected error"
    }
)
@api_view(["POST", "GET"])
def order(request):
    if request.method == "POST":
        return create_order(request)
    elif request.method == "GET":
        return get_orders(request)

def get_orders(request):
    try:
        id = request.GET.get('id')
        if id:
            order = Order.objects.filter(catering = id)
            order_serializer = OrderViewSerializer(order, many=True).data
            return JsonResponse(order_serializer, status=status.HTTP_200_OK, safe=False)
        elif request.user_id:
            order = Order.objects.filter(ordered_by = request.user_id)
            serializer_order = OrderViewSerializer(order, many=True).data
            return JsonResponse(serializer_order, status=status.HTTP_200_OK, safe=False)
    except AttributeError:
        return JsonResponse({"message":"Access denied!"}, status=status.HTTP_403_FORBIDDEN)
    except Exception as e :
        return JsonResponse({"message": "Oops something went wrong", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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