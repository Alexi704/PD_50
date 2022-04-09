import pytest

from forge.forge3 import Player

def test_player():
    player = Player()
    value = 25
    player.set_score(value)
    assert player.get_score() == value