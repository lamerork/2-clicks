import requests

def get_weather():

        cities = ['Шереметьево',
                'Лондон',
                'Череповец']

        url = 'https://wttr.in/'
        
        params_dict = {'nTqM': '',
                  'lang': 'ru'}

        for city in cities:
                response = requests.get(url + city, params=params_dict)
                response.raise_for_status()
                print(response.text)

if __name__ == '__main__':
        get_weather()