from django.shortcuts import render
from django.http import JsonResponse
from .models import Diagnostic, Region, User

def read_all_diagnostics(request):
    all_records = Diagnostic.objects.all()
    
    data = [{'name': record.name, 'description': record.description} for record in all_records]
    
    return JsonResponse({'data': data})

def read_all_regions(request):
    all_records = Region.objects.all()
    
    data = [{'name': record.name} for record in all_records]
    
    return JsonResponse({'data': data})
