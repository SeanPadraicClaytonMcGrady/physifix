from django.shortcuts import render
from django.http import JsonResponse
from .models import Diagnostic

# def home(request):
#     return HttpResponse("Hello, world. You're at the physifix index.")

def read_all(request):
    all_records = Diagnostic.objects.all()
    
    data = [{'name': record.name, 'description': record.description} for record in all_records]
    
    return JsonResponse({'data': data})