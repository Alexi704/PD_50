from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def page_form():
    return render_template('task2.html')


@app.route('/add', methods=['POST'])
def page_name():
    username = request.form.get('username')
    level = request.form.get('level')
    with open('records.txt', 'a', encoding='utf-8') as file:
        file.write(f'{username} - {level}\n')
    return 'файл записан!!!'


app.run()
