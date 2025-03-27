from django.urls import path
from .views import *

urlpatterns = [
    path('login/', sign_in, name='login-url'),
    path('logout/',sign_in, name='logout-url'),
    path('register/', register name='register-url'),   
]