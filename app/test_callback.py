# -*- coding: utf-8 -*-
from flask import Flask, request
import vk_api
import json
from vk_api.utils import get_random_id

with open('secret.json', 'r') as j:
        text = j.read()
        list_of_secrets = json.loads(text)

app = Flask(__name__)
vk_session = vk_api.VkApi(token= list_of_secrets["token"])
vk = vk_session.get_api()

confirmation_code = list_of_secrets["confirm_token"]

"""
При развертывании путь к боту должен быть секретный,
поэтому поменяйте my_bot на случайную строку

Например:
756630756e645f336173313372336767

Сгенерировать строку можно через:
$ python3 -c "import secrets;print(secrets.token_hex(16))"
"""
@app.route('/', methods=['POST'])
def bot():
    # получаем данные из запроса
    data = request.get_json(force=True, silent=True)
    print(data)
    # ВКонтакте в своих запросах всегда отправляет поле type:
    if not data or 'type' not in data:
        return 'not ok'
    
    # проверяем тип пришедшего события
    if data['type'] == 'confirmation':
        print("CONFIRMATION")
        # если это запрос защитного кода
        # отправляем его
        return confirmation_code

    return 'ok'  # игнорируем другие типы

if __name__ == '__main__':
    app.run()

