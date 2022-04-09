from flask import Flask

app = Flask(__name__)

words = ["@кот", "@хлеб", "не", "ешь", "@подумай", "теперь", "ешь"]

@app.route('/mentions', )
def page_index_mentions():
    mentions = []
    for word in words:
        if word.startswith('@'):
            mentions.append(word[1:])
    output = ' '.join(mentions)
    return output

app.run()


"""
У вас есть список слов в которых есть упоминания типа @cat
words = ["@кот", "@хлеб", "не", "ешь", "@подумай", "теперь", "ешь"]
Напишите вьюшку /mentions, которая вытаскивает слова, 
которые начинаются с собачки и возвраает их
Пример вывода:  кот хлеб подумай

"""