from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/hello', )
def page_index():
    return "hello"


@app.route('/goodbye', )
def page_goodbye():
    return "goodbye"


@app.route('/seeyou', )
def page_seeyou():
    return "seeyou"



app.run()
