import requests
import random

def request_word():
    words_url = 'https://api.datamuse.com/words'
    params = {
        'sp': '?????',
        'max': 1000
    }
    response = requests.get(url = words_url, params=params)

    if response.status_code == 200:
        data = response.json()
    else:
        print(f'Failed to retrieve data from {words_url}')

    random_item = random.choice(data)

    random_word = random_item["word"]
    print(type(random_word))
    return random_word
request_word()