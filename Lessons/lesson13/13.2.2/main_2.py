from flask import Flask

app = Flask(__name__)


@app.route("/")
def demo_json():
    return "it works"


if __name__ == "__main__":
    app.run()

response = app.test_client().get('/')

# assert response.status_code == 200
# assert response.data == b'it works!'
