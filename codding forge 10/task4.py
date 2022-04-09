from flask import Flask

app = Flask(__name__)

numbers = [23, 16, 144, 72, 90, 11, 5]

@app.route('/first', )
def page_index_first():
    return str(numbers[0])

@app.route('/last', )
def page_index_last():
    return str(numbers[-1])

@app.route('/sum', )
def page_index_sum():
    return str(sum(numbers))

app.run()


