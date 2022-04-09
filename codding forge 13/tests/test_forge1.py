import pytest

from forge.forge1 import get_cat_facts

def test_get_cat_facts():
    response = get_cat_facts()
    assert response.get('fact')
    assert response.get('length')