import pytest
from unittest.mock import MagicMock

from dao.director import DirectorDAO
from service.director import DirectorService

from dao.genre import GenreDAO
from service.genre import GenreService

from dao.movie import MovieDAO
from service.movie import MovieService


##################### фикстуры под режиссеров #####################
@pytest.fixture
def director_dao():
    # глушим DAO
    dao = DirectorDAO(None)
    dao.get_one = MagicMock()
    dao.get_all = MagicMock()
    dao.update = MagicMock()
    dao.delete = MagicMock()
    return dao


@pytest.fixture
def director_service(director_dao):
    return DirectorService(dao=director_dao)


##################### фикстуры под жанры #####################
@pytest.fixture
def genre_dao():
    # глушим DAO
    dao = GenreDAO(None)
    dao.get_one = MagicMock()
    dao.get_all = MagicMock()
    dao.update = MagicMock()
    dao.delete = MagicMock()
    return dao


@pytest.fixture
def genre_service(genre_dao):
    return GenreService(dao=genre_dao)


##################### фикстуры под фильмы #####################
@pytest.fixture
def movie_dao():
    # глушим DAO
    dao = MovieDAO(None)
    dao.get_one = MagicMock()
    dao.get_all = MagicMock()
    dao.update = MagicMock()
    dao.delete = MagicMock()
    return dao


@pytest.fixture
def movie_service(genre_dao):
    return MovieService(dao=genre_dao)
