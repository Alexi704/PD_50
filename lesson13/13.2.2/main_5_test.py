import pytest
from main_5 import app


def test_json():
    data = {"name": "Alice2"}
    response = app.test_client().post('/', json=data, follow_redirects=True)
    assert response.json == {"name_received": "Alice2"}
