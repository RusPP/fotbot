from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import random
import os
# import wikipedia
import time

# константы и настройки
wikipedia.set_lang("RU")
token = '84b2dd8f3ea44de2d3564b15c123338aa4f713973dd9b0f7f9fd332c539df5b082dad8cca2a7ab1a7411b'
vk_session = vk_api.VkApi(token=token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


# функция отправки сообщений
def send_message(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send',
                      {id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648),
                       "attachment": None, 'keyboard': None})



# отклик на ивенты
for event in longpoll.listen():
    # работа с википедией
    try:
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            if event.text == 'Википедия' or event.text == 'Вики' or event.text == 'википедия' or event.text == 'вики' or event.text == 'Wikipedia' or event.text == 'wikipedia' or event.text == 'Wiki' or event.text == 'wiki':
                if event.from_user:
                    send_message(vk_session, 'user_id', event.user_id, message="Что найти?")
                elif event.from_chat:
                    send_message(vk_session, 'chat_id', event.chat_id, message="Что найти?")
                continue
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
           if event.from_user:
               send_message(vk_session, 'user_id', event.user_id,
                           message="Вот что я нашёл: \n" + str(wikipedia.summary(event.text)))
            elif event.from_chat:
                send_message(vk_session, 'chat_id', event.chat_id,
                            message="Вот что я нашёл: \n" + str(wikipedia.summary(event.text)))

    except wikipedia.exceptions.PageError:
        if event.from_user:
            send_message(vk_session, 'user_id', event.user_id, message="Я ничего не смог найти")
    
    except wikipedia.exceptions.DisambiguationError:
        if event.from_user:
            send_message(vk_session, 'user_id', event.user_id, message="Я ничего не смог найти")
        elif event.from_chat:
           send_message(vk_session, 'chat_id', event.chat_id, message="Я ничего не смог найти")
