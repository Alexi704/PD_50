from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def receive_data_from_json():
    data = request.json

    with open("data_3.txt", "w", encoding="utf-8") as file:
        file.write(data.get("name") + "\n")
        file.write(data.get("phone") + "\n")
        file.write(data.get("email") + "\n")

    return jsonify("Данные записаны")


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run()
