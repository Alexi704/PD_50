from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def page_load_file():
    if request.method == 'POST':
        file = request.files['file']
        file.save(f'uploads/{file.filename}')
        return 'файл загружен'
    return render_template('index4.html')


app.run()
