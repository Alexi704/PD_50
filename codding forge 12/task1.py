from flask import Flask, request, render_template

app = Flask(__name__)

ws = [
    "платина", "стена", "халат", "блокнот", "косилка",
    "автобус", "базар", "биосфера", "грелка"
]


@app.route('/')
def form_page():
    return render_template('index.html')

@app.route('/search')
def search_page():
    query = request.values.get('search_input')
    result = []
    for item in ws:
        if query in item:
            result.append(item)
    result_str = '<br/>'.join(result)
    return result_str


app.run()
