from django.shortcuts import render, redirect
from .models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate 
# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            User.objects.create(username=username, password=password)
        except:
            return HttpResponse('bu username band')
        return redirect('login-url')
    
def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request, usr)
            return redirect('index-url')
        else:
            return HttpResponse('username yoki password xato')
        
def sign_out(request):
    logout(request)
    return redirect('login-url')
        
