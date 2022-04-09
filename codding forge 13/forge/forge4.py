import requests


def get_cat_facts(number):
    facts_list = []
    for _ in range(number):
        data = requests.get('https://catfact.ninja/fact')
        result = data.json()
        facts_list.append(result)
    return facts_list


# print(get_cat_facts())
