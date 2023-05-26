import requests

def get_weather():

        urls = ['https://wttr.in/Шереметьево?nTqM&lang=ru', 
                'https://wttr.in/Лондон?nTqM&lang=ru',
                'https://wttr.in/Череповец?nTqM&lang=ru']

        for url in urls:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)

