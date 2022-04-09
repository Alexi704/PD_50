from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', )
def page_index():
    user = {"username": "alexy_001", "email": "alexy@skyeng.ru", "phone": "+1555223311"}
    return render_template('index.html', user=user)


@app.route('/city', )
def page_city():
    cities = {1: "Самара", 2: "Краснодар", 3: "Сочи", 4: "Новосибирск", 5: "Вышгород"}
    return render_template('city.html', cities=cities)

if __name__ == '__main__':
    app.run()
