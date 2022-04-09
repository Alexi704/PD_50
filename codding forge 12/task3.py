from flask import Flask, request, render_template

app = Flask(__name__)

LOGIN = 'Admin'
PASSWORD = 'Pas7931'


@app.route('/')
def page_form():
    return render_template('task3.html')


@app.route('/login', methods=['POST'])
def page_login():
    user_login = request.form.get('username')
    user_pswd = request.form.get('password')
    if user_login == LOGIN and user_pswd == PASSWORD:
        return "Вход разрешен"
    return "Вход запрещен"


app.run()
