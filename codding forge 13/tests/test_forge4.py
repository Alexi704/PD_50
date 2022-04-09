import pytest

from forge.flask4 import app

def test_cats_app():
    value = 5
    response = app.test_client().get(f'/cats/{value}')
    print(response.json)