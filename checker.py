from random import choice
from urllib import request
from http.client import IncompleteRead
from time import sleep

wait_time = 0.3  # Увеличили задержку между запросами
separator = ' | '
base_url = 'http://steamcommunity.com/id/'

def pad_right(string, n_chars):
    return string + (' ' * (n_chars - len(string)))

class Id:
    def __init__(self, url):
        req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        for attempt in range(3):  # Повторяем до 3 раз в случае ошибки
            try:
                response = request.urlopen(req, timeout=10)  # Увеличенный timeout
                html = response.read().decode('utf-8')
                break  # Если успешно, выходим из цикла
            except IncompleteRead as e:
                html = e.partial.decode('utf-8')  # Используем частично загруженные данные
                print(f'Warning: IncompleteRead, attempt {attempt+1}')
                sleep(1)  # Пауза перед новой попыткой
            except Exception as e:
                print(f'Error: {e}, attempt {attempt+1}')
                sleep(1)
                html = ''
        
        self.exist = 'The specified profile could not be found.' not in html

def gen_word(words):
    words = words.split('\n')
    return choice(words).strip()

if __name__ == '__main__':
    print(f'config:\n        wait_time = {wait_time}\n        separator = {separator}\n        list = list.txt')

    with open('list.txt') as f:
        words = f.read()
    
    open('available_ids.txt', 'w').close()

    while True:
        url = base_url + gen_word(words)
        curr = Id(url)
        url_space = len(base_url) + 15
        url = pad_right(url, url_space)
        s = separator

        if not curr.exist:
            print(f'{url}{s}not taken')
            with open('available_ids.txt', 'a') as out_file:
                out_file.write(url[len(base_url):].strip() + '\n')
        else:
            print(f'{url}{s}taken')

        sleep(wait_time)