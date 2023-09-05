# -*- coding: utf-8 -*-
import json
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

def main():
    with open('secret.json', 'r') as j:
        text = j.read()
        list_of_secrets = json.loads(text)

    #TOKEN
    vk_session = vk_api.VkApi(token = list_of_secrets["token"])
    #FROUP_ID
    longpoll = VkLongPoll(vk=vk_session, group_id=list_of_secrets["group_id"])

    #START

    for event in longpoll.listen():

        if event.type == VkEventType.MESSAGE_NEW:
            print('Новое сообщение:')

            if event.to_me:
                print('Для меня от: ', end='')

            if event.from_user:
                print(event.user_id)

            print('Текст: ', event.text)
            print()

        else:
            print(event.type, event.raw[1:])


if __name__ == '__main__':
    main()