from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Diagnostic, Region, User
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password

def read_all_diagnostics(request):
    all_records = Diagnostic.objects.all()
    
    data = [{'name': record.name, 'description': record.description} for record in all_records]
    
    return JsonResponse({'data': data})

def read_all_regions(request):
    all_records = Region.objects.all()
    
    data = [{'name': record.name} for record in all_records]
    
    return JsonResponse({'data': data})

def sign_in(request):
    
    if request.method == 'POST':
        data = request.POST
        
        username = data.get('username')
        password = data.get('password')
        
        user = authenticate(username=username, password=password)
        
        print(user, "user heeeeeeeeeeeeeeeeeeeeeeeeeeeeere")
    
        if user is not None:
            login(request, user)
            return HttpResponse("Sign-in successful")
        else: 
            return HttpResponse("Sign-in failed.")
    
    
