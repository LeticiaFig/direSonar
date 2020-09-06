from django.http import JsonResponse
from django.shortcuts import render

def event(requests):
    print(requests)
    return JsonResponse({'name': 'Letícia', 'profissão': 'dev'})
