from django.conf.urls import url
from api.Views import user_views, catering_views, order_views
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register/', user_views.register),
    path('activate', user_views.activate_email),
    path('login', user_views.login),
    path('register/seller', user_views.seller_register),
    
    path('user', user_views.user),
    path('catering', catering_views.catering),
    path('order', order_views.order),
]