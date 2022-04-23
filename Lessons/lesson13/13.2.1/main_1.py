from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def get_json():
    data = {"name": "Алиса"}
    return jsonify(data)


if __name__ == '__main__':
    app.run()
