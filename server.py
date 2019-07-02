import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from book_bot import BookBot
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

# Бот для каждого пользователя, с которым переписываемся
bots = {}

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
    
        # Если оно имеет метку для меня(то есть бота)
        if event.to_me:
            print('Мне пришло сообщение')

            # Сообщение от пользователя
            request = event.text

            print('Пришло сообщение')
            print('От: ', event.user_id)

            if not (event.user_id in bots.keys()):
                bots[event.user_id] = BookBot(event.user_id)

            bot = bots[event.user_id]
            message, random_id = bot.new_message(event.text)

            write_msg(event.user_id, message, random_id)
            
            print('Text: ', event.text)