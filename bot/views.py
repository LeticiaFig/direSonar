import random

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .util import send_message, process_message, send_message_onlyText
from core.models import Interaction
import json
import time


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

    if command == "Receber direcionamento":
        senha = random.randint(100, 200)
        output = "Siga em frente por 10 metros e depois vire a direita e caminhe por mais 3 metros. Em seguida, à sua direita, estarão as cadeiras e a, à sua esquerda, estará o balcão de atendimento. Sua senha é {0}, a senha atual é {1}. Você receberá mensagens com o andamento da fila.".format(senha, senha-3)
        send_message_onlyText(chat_id, output)
        time.sleep(random.randint(1, 30))
        output = "Senha atual: {0}\nVocê será atendido em breve".format(senha-2)
        send_message_onlyText(chat_id, output)
        time.sleep(random.randint(1, 45))
        output = "Senha atual: {0}\nVocê é o próximo da fila!".format(senha-1)
        send_message_onlyText(chat_id, output)
        time.sleep(random.randint(1, 60))
        output = "Senha atual: {0}\nSua vez chegou!".format(senha)
        send_message_onlyText(chat_id, output)
    else:
        output = process_message(command)
        send_message(chat_id, output)

    # if command == "Confirmar":
    #     time.sleep(120)
    #     output.text = "Olá! Você possui uma consulta agendada para o dia 15/09 às 11:00. Posso confirmar?"
    #     output.button = "Sim, Não"
    #     send_message(chat_id, output)
    #     time.sleep(120)
    #     output.text = "Olá! Não se esqueça da sua consulta com o Dr Arthur hoje às 11:00. Quando chegar na clínica, clique no botão abaixo escrito Cheguei"
    #     output.button = "Cheguei"
    #     send_message(chat_id, output)

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

