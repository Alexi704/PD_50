import random
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/random', )
def page_index():
    a = random.randint(0,10)
    return str(a)


app.run()
