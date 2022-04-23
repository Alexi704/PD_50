import pytest

from main_3 import app


def test_app():
    response = app.test_client().get('/')
    assert response.json.get("name") == "Алиса", "Имя получено неверно"
