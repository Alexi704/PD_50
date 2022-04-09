from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', )
def page_index():
    cities = {1: "Самара", 2: "Краснодар", 3: "Сочи", 4: "Новосибирск", 5: "Вышгород"}
    return render_template('index.html', cities=cities)

app.run()