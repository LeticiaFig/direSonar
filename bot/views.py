import random

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .util import send_message, process_message, send_message_onlyText
from core.models import Interaction
import json
import time
import sys

@csrf_exempt
def event(requests):
    print(requests)
    json_list = json.loads(requests.body)
    print(json_list)
    if "message" in json_list:
        chat_id = json_list['message']['chat']['id']
        command = json_list['message']['text']
    elif "edited_message" in json_list:
        chat_id = json_list['edited_message']['chat']['id']
        command = json_list['edited_message']['text']

    output = process_message(command)
    send_message(chat_id, output)

    return HttpResponse()


@csrf_exempt
def res(requests, response):
    print("ENTROU AQUI")

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

