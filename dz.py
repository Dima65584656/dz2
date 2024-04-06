import requests


def get_random_cat_fact():
    url = "https://cat-fact.herokuapp.com/facts/random"
    response = requests.get(url)

    if response.status_code == 200:
        fact = response.json()['text']
        return fact
    else:
        return "Не удалось получить факт о котах"


print(get_random_cat_fact())
