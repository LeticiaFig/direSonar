import requests, json
from core.models import Interaction

TOKEN = '1380220570:AAHOzP_pH17JWCnqoZ5T68Dki4Lh8Lobico'


def process_message(command):
    interaction = Interaction.objects.get(input=command)
    if interaction.execute_script:
        dic = interaction.execute()
        output = interaction.get_output(dic)
    else:
        output = interaction.output
    return output


def send_message(chat_id, text):
    url = 'https://api.telegram.org/bot{0}/sendMessage'.format(TOKEN)
    data = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, data=data)
    results = r.json()
    print(results)


def send_message_with_button(chat_id, text, buttons):
    url = 'https://api.telegram.org/bot{0}/sendMessage'.format(TOKEN)
    reply_markup = {"keyboard": [["Yes", "No"], ["Maybe"], ["1", "2", "3"]], "one_time_keyboard": True}
    data = {'chat_id': chat_id, 'text': text, 'reply_markup': json.dumps(reply_markup)}
    r = requests.get(url, data=data)
    results = r.json()
    print(results)



