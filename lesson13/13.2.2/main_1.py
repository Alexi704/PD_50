from flask import Flask

app = Flask(__name__)


@app.route("/")
def demo_json():
    return "it works"


response = app.test_client().get('/')

print(response.status_code)
print(response.data)
