# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from decouple import config
import requests


def dashboard(request):
    return HttpResponse("Hello")


def complain(request):
    latitude = request.GET['lat']
    longitude = request.GET['lon']
    text = request.GET['text']
    category = request.GET['category']
    # TODO: Store in DB model
    result = {
        "messages": [
            {"text": "{}: {}: {}: {}".format(latitude, longitude, text, category)}
        ]
    }
    return JsonResponse(result)


def broadcast(request):
    bot_id = config('BOT_ID')
    chatfuel_token = config('CHATFUEL_TOKEN')
    user_id = '1813643665334588'
    block_name = 'broadcast'
    message = 'Your complain has been forwarded to the concerned authority.'
    endpoint = "https://api.chatfuel.com/bots/{}/users/{}/send?chatfuel_token={}&chatfuel_block_name={}&message={}" \
        .format(bot_id, user_id, chatfuel_token, block_name, message)
    r = requests.post(endpoint)
    return HttpResponse(r.status_code)
