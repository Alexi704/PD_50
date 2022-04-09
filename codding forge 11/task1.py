from flask import Flask, request, render_template
import random

app = Flask(__name__)


@app.route('/python', )
def page_python():
    return "python - это язык который мы учим"

@app.route('/java', )
def page_java():
    return "java - а это мы не учим"

@app.route('/php', )
def page_php():
    return "а это что такое вообще"

@app.route('/random', )
def page_random():
    alphabet = 'ABCDEFGHIKLMNOPQRSTVXYZ'
    letter = random.choice(alphabet)
    return letter


@app.route('/detect/<value>', )
def page_detect(value):
    if value.isdigit():
        result = 'это число'
    else:
        result = 'это не число'
    return result













if __name__ == '__main__':
    app.run()
