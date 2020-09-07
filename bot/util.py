import requests, json
from sqlparse.filters import output

from core.models import Interaction

TOKEN = '1308541770:AAFvpq8721iZLAaCq9Gm3UROwTGRzanZlaM'


def process_message(command):
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
        output.hasButton = False

    return output


def send_message(chat_id, output):
    url = 'https://api.telegram.org/bot{0}/sendMessage'.format(TOKEN)

    if output.hasButton:
        preButtons = (output.buttons).split(',')
        buttons = []
        for el in preButtons:
            sub = el.split(', ')
            buttons.append(sub)

        reply_markup = {"keyboard": buttons, "one_time_keyboard": True}
        data = {'chat_id': chat_id, 'text': output.text, 'reply_markup': json.dumps(reply_markup)}
        r = requests.get(url, data=data)

    else:
        data = {'chat_id': chat_id, 'text': output.text}
        r = requests.post(url, data=data)

    results = r.json()
    print(results)


def send_message_with_button(chat_id, text, buttons):
    url = 'https://api.telegram.org/bot{0}/sendMessage'.format(TOKEN)
    reply_markup = {"keyboard": [buttons], "one_time_keyboard": True}
    data = {'chat_id': chat_id, 'text': text, 'reply_markup': json.dumps(reply_markup)}
    r = requests.get(url, data=data)
    results = r.json()
    print(results)



