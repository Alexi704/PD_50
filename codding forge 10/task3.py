from flask import Flask

app = Flask(__name__)

words = {"one":"один", "two": "два", "three": "три"}

@app.route('/one', )
def page_index_one():
    return words['one']

@app.route('/two', )
def page_index_two():
    return words['two']

@app.route('/three', )
def page_index_three():
    return words['three']

app.run()


