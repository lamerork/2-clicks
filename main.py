import requests

def main():

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
        main()