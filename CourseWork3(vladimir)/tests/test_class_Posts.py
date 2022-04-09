import pytest
from flask import Flask

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def demo_text():
    return "anything text"

class TestPosts:
    def test_get_posts_all(self):
        response = app.test_client().get('/')
        assert response.status_code == 200
        assert response.data == b'anything text'

    # def test_get_posts_by_user(self):
    #     user_name = 'user_name'
    #     posts = Posts(user_name)
    #     response = app.test_client().get('/username')
    #     assert response.json.get(user_name) == 'user_name', 'Ошибка в имени'
