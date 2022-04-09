from flask import Flask

app = Flask(__name__)

content = "Кот это не хлеб, подумай, не ешь его, разработчик! Ай, ну я же просил"
spaces = content.count(' ')
words_count = spaces + 1

letter_counter = 0
for item in content:
    if item.isalpha():
        letter_counter +=1


@app.route('/words', )
def page_index_words():
    return str(words_count)

@app.route('/spaces', )
def page_index_spaces():
    return str(spaces)

@app.route('/letters', )
def page_index_letters():
    return str(letter_counter)


app.run()


"""
У вас есть текст
content = "Кот это не хлеб, подумай, не ешь его, разработчик! Ай, ну я же просил"
Напишите вьюшки
/words - подсчитывает слова, например:  11 слов
/spaces - подсчитывает пробелы, например 10 пробелов
/letters – подсчитывает количество букв, например 35 букв
Пример вывода:  
"""