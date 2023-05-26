import requests

def get_weather():

        urls = ['https://wttr.in/Шереметьево', 
                'https://wttr.in/Лондон',
                'https://wttr.in/Череповец']
        
        params_dict = {'nTqM': '',
                  'lang': 'ru'}

        for url in urls:
                response = requests.get(url, params=params_dict)
                response.raise_for_status()
                print(response.text)

if __name__ == '__main__':
        get_weather()