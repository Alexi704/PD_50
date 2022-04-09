from flask import Flask

app = Flask(__name__)


@app.route("/")
def page_index():
    pass


@app.route("/post", methods=["GET", "POST"])
def page_post_form():
    pass


if __name__ == "__main__":
    app.run()
