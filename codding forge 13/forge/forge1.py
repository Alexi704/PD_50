import requests

def get_cat_facts():
    data = requests.get('https://catfact.ninja/fact')
    result = data.json()
    return result


print(get_cat_facts())
