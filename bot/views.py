from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .util import send_message, process_message
from core.models import Interaction
import json


@csrf_exempt
def event(requests):
    print(requests)
    json_list = json.loads(requests.body)
    print(json_list)
    chat_id = json_list['message']['chat']['id']
    command = json_list['message']['text']

    output = process_message(command)
    send_message(chat_id, output)

    return HttpResponse()


@csrf_exempt
def teste(requests):
    print(requests)
    json_list = json.loads(requests.body)
    print(json_list)
    chat_id = json_list['message']['chat']['id']
    command = json_list['message']['text']
    text = json_list['message']['text']

    output = process_message(command)
    send_message(chat_id, "Deu bom")

