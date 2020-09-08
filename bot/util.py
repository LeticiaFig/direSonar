import requests, json
from sqlparse.filters import output

from core.models import Interaction

TOKEN = '1308541770:AAH_KomvXIbhdQCGzxSpHBtTdoklm98aSOw'


def process_message(command):
    output.input = command
    try:
        interaction = Interaction.objects.get(input=command)
        output.hasButton = interaction.hasButton
        if output.hasButton:
            output.buttons = interaction.buttons
        if interaction.execute_script:
            dic = interaction.execute()
            output.text = interaction.get_output(dic)
        else:
            output.text = interaction.output

    except Interaction.DoesNotExist:
        output.text = "Comando não encontrado, envie 'ajuda' para receber orientações!"
        output.hasButton = True
        output.buttons = "Agendamentos, Minha Agenda|Cancelamentos, Ajuda"

    return output


def send_message(chat_id, output):
    url = 'https://api.telegram.org/bot{0}/sendMessage'.format(TOKEN)

    if output.hasButton:
        preButtons = (output.buttons)

        buttons = [preButtons.split(',') for preButtons in preButtons.split('|')]
        formattedbutton = [[json.loads(json.dumps({'text': btn, "url":"https://9ea17fbbbdeb.ngrok.io/bot/response/"+btn})) for btn in button] for button in buttons]

        reply_markup = {"keyboard": formattedbutton, "one_time_keyboard": True}
        data = {'chat_id': chat_id, 'text': output.text, 'reply_markup': json.dumps(reply_markup)}
        r = requests.get(url, data=data)
        print(r)

    else:
        data = {'chat_id': chat_id, 'text': output.text}
        r = requests.post(url, data=data)

    results = r.json()
    print(results)


def send_message_onlyText(chat_id, text):
    url = 'https://api.telegram.org/bot{0}/sendMessage'.format(TOKEN)
    data = {'chat_id': chat_id, 'text':text}
    r = requests.post(url, data=data)
    results = r.json()
    print(results)


