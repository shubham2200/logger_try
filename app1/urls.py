from .views import *
from django.contrib import admin
from django.urls import path 



urlpatterns = [
    path('',sign_up,name='sign_up'),
    path('login/',login_page,name='login_page' ),
    path('details/',details,name='details'),
    path('logout_user/',logout_user, name="logout_user")
]
