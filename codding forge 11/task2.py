from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', )
def page_python():
    return "python - это язык который мы учим"










if __name__ == '__main__':
    app.run()
