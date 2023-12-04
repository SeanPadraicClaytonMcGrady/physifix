from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Diagnostic, Region, User
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
import json

def read_all_diagnostics(request):
    all_records = Diagnostic.objects.all()
    
    data = [{'name': record.name, 'description': record.description} for record in all_records]
    
    return JsonResponse({'data': data})

def read_all_regions(request):
    all_records = Region.objects.all()
    
    data = [{'name': record.name} for record in all_records]
    
    return JsonResponse({'data': data})

def read_all_users(request):
    all_users = User.objects.all()
    
    data = [{'email': record.email, 'first_name': record.first_name, 'last_name': record.last_name} for record in all_users]
    
    return JsonResponse({'data': data})

def log_in(request):
    
    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
        else: 
            data = request.POST
            username = data.get('username')
            password = data.get('password')
            
            
        user = authenticate(username=username, password=password)
    
        if user is not None:
            login(request, user)
            return JsonResponse({"message" : "Sign-in successful"})
        else: 
            return JsonResponse({"error:" "Sign-in failed."})
    
    
