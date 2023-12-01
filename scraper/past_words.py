import requests
from bs4 import BeautifulSoup
import random
# import datetime
# import sched
# import time


def get_random_word():
    """
    Scrapes website to retreive a list of 5 letter words.
    """
    words = []
    url = "https://www.rockpapershotgun.com/wordle-past-answers/"

    # GET request to retreive the web page
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        ul_element = soup.find('ul', class_='inline')

        li_elements = ul_element.findChildren("li" , recursive=False)

        words = [li.text for li in li_elements]

    else:
        print("Failed to retrieve the web page. Status code:", response.status_code)
        return

    return random.choice(words)

# USE TO REPEATEDLY RUN AT SPECIFIED INTERVAL (SECONDS)
# s = sched.scheduler(time.time, time.sleep)
# interval = 5

# while True:
#     s.enter(interval, 1, past_words, ())
#     s.run()



# print(type(get_random_word()), get_random_word())
