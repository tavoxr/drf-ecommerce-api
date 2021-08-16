from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hola</h1>')
