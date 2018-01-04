# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def dashboard(request):
    return HttpResponse("Hello")


def complain(request):
    latitude = request.GET['lat']
    longitude = request.GET['lon']
    text = request.GET['text']
    category = request.GET['category']
    # return HttpResponse(request.GET.values())
    result = {
        "messages": [
            {"text": "Thank you. Your complain has been registered."}
        ]
    }
    return JsonResponse(result)