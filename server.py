import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from config import api_key

def write_msg(user_id, message, random_id):
    vk.method('messages.send', {
        'user_id': user_id,
        'message': message,
        'random_id': random_id
    })

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=api_key)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

print('Сервер слушает')

message_id = 0

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
    
        # Если оно имеет метку для меня(то есть бота)
        if event.to_me:
            print('Мне пришло сообщение')

            # Сообщение от пользователя
            request = event.text

            # Каменная логика ответа
            if request == "привет":
                write_msg(event.user_id, "Привет с:", message_id)
            elif request == "пока":
                write_msg(event.user_id, "Пока :с", message_id)
            else:
                write_msg(event.user_id, "Непонятно", message_id)

            message_id += 1