import pytest

from utils_7 import Player

name = 'Anna'

class TestPlayer:

    def test_change_name(self):
        player = Player(name)
        player.change_name('Li')
        assert player.name == 'Li', 'Ошибка при изменении имени'

    def test_add_points(self):
        player = Player(name)
        player.add_points(10)
        assert player.points == 10, "Ошибка в начислении очков"

    def test_get_points(self):
        player = Player(name)
        player.points = 5
        assert player.get_points() == 5, "Ошибка в считывании очков"

    def test_init_type_error(self):
        with pytest.raises(TypeError):
            Player()

