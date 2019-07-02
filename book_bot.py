import bs4
import requests
import random

class BookBot:

    def __init__(self, user_id):
    
        print('Создан объект бота!')
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)
        self._RANDOM_ID = random.randint(0,100000)
        
        self._COMMANDS = ['ПРИВЕТ', 'ЧТО ПОЧИТАТЬ?', 'ПОКА']

    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get('https://vk.com/id'+str(user_id))
        bs = bs4.BeautifulSoup(request.text, 'html.parser')
        
        user_name = self._clean_all_tag_from_str(bs.findAll('title')[0])
        
        return user_name.split()[0]

    @staticmethod
    def _clean_all_tag_from_str(string_line):
        '''
        Очистка строки stringLine от тэгов и их содержимых
        :param string_line: Очищаемая строка
        :return: очищенная строка
        '''
        result = ''
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == '<':
                    not_skip = False
                else:
                    result += i
            else:
                if i == '>':
                    not_skip = True
        
        return result

    def new_message(self, message):
        self._RANDOM_ID += 1

        if message.upper() == self._COMMANDS[0]:
            return 'Привет, ' + self._USERNAME + ' c:', self._RANDOM_ID

        elif message.upper() == self._COMMANDS[1]:
            return 'Выбираю книгу...', self._RANDOM_ID

        elif message.upper() == self._COMMANDS[2]:
            return 'Пока, ' + self._USERNAME, self._RANDOM_ID
        
        else:
            return 'Не понимаю о чем вы...', self._RANDOM_ID