from flask import Flask, jsonify

from forge.forge4 import get_cat_facts

app = Flask(__name__)


@app.route('/cats/<int:number>')
def page_cat(number):
    cats_list = get_cat_facts(number)
    return jsonify(cats_list)

if __name__ == '__main__':
    app.run()