from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

list_of_words = ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]


@app.route("/")
def get_json():
    return jsonify(list_of_words)


if __name__ == '__main__':
    app.run()
