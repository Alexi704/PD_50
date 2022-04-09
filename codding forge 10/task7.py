from flask import Flask
import json

with open('file.json', 'r', encoding='utf-8') as file:
    numbers = json.load(file)

app = Flask(__name__)

@app.route('/first', )
def page_index_first():
    return str(numbers[0])


@app.route('/last', )
def page_index_last():
    return str(numbers[-1])


@app.route('/sum', )
def page_index_sum():
    return str(sum(numbers))


app.run()

"""
У вас есть файл JSON, где хранятся числа
[1,17,22,94]
Напишите три вьюшки 
/first - выведет первое число
/last - выведет последнее число 
/sum - выведет сумму чисел
```
"""
