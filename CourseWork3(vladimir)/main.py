from flask import Flask, render_template
from web.bp_views import blueprint_web
from api.bp_views import blueprint_api
from pprint import pprint as pp

app = Flask(__name__)
app.register_blueprint(blueprint_web)
app.register_blueprint(blueprint_api)
app.config['JSON_AS_ASCII'] = False


@app.route("/")
def page_index():
    pass


@app.route('/search')
def search_page():
    pass


if __name__ == "__main__":
    app.run()
