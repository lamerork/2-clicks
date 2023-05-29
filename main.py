
import requests
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")
MAINLINK = os.getenv('MAINLINK')

def shorten_link(token, link):

    headers = {
    'Authorization': token,
    'Content-Type': 'application/json',
    }

    data = '{"long_url": "' + link + '"}'

    response = requests.post(MAINLINK, headers=headers, data=data)
    response.raise_for_status()
    bitlink = response.json()

    return bitlink['id']

def get_link():
    user_link = input('Введите ссылку: ')
    return user_link

def count_clicks(token, link):

    headers = {
    'Authorization': token,
    'Content-Type': 'application/json',
    }

    params = {
        'unit': 'day',
        'units': '-1'
    }

    response = requests.get(MAINLINK + link + '/clicks/summary', params=params, headers=headers)
    print(response.url)
    response.raise_for_status()
    click_count = response.json()

    return click_count['total_clicks']

def is_bitlink(url):
    
    if url[:6] == 'https:' or url[:5] == 'http:':
        return True
    return False

def main():

    user_link = get_link()

    try:
        
        if is_bitlink(user_link):
            print('Битлинк:', shorten_link(TOKEN, user_link))

        else:
            print('Клики:', count_clicks(TOKEN, user_link))

    except requests.exceptions.HTTPError:
        print("Ошибка! Неверная ссылка")

if __name__ == '__main__':
    
    main()
