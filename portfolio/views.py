from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Hello from Portfolio Home!")


def api_view(request):
    return HttpResponse("Hello this is the api view")