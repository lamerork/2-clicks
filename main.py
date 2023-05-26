import requests

def get_weather():

        cities = ['Шереметьево',
                'Лондон',
                'Череповец']
        params_dict = {'nTqM': '',
                  'lang': 'ru'}

        url = 'https://wttr.in/'

        for city in cities:
                response = requests.get(url + city, params=params_dict)
                response.raise_for_status()
                print(response.text)
                print(response.url)

if __name__ == '__main__':
        get_weather()