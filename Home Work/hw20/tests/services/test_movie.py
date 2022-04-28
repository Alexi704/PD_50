import pytest
from unittest import mock


class MovieNotFound(Exception):
    pass


# можно параметры не выносить, а прописывать в фикструре
parametrize = (
    {'id': 1,
     'title': mock.ANY,
     'description': mock.ANY,
     'trailer': mock.ANY,
     'year': 1999,
     'rating': 9, },
)


@pytest.mark.parametrize('data', parametrize)
def test_get_one(movie_service, data):
    """ Тестирование функции get_one() """
    movie_service.dao.get_one.return_value = data

    assert movie_service.get_one(data['id']) == data


def test_get_one_with_error(movie_service):
    """ Тестируем функцию  get_one() на наличие ошибки в передаваемом id """
    movie_service.dao.get_one.side_effect = MovieNotFound
    with pytest.raises(MovieNotFound):
        movie_service.get_one(0)
        movie_service.get_one(-1)
        movie_service.get_one(1.5)
        movie_service.get_one('any_str')


parametrize = (
    (2, [
        {'id': 1,
         'title': mock.ANY,
         'description': mock.ANY,
         'trailer': mock.ANY,
         'year': 1999,
         'rating': 9, },
        {'id': 2,
         'title': mock.ANY,
         'description': mock.ANY,
         'trailer': mock.ANY,
         'year': 2008,
         'rating': 8, },
    ],),
    (0, [],),
)


@pytest.mark.parametrize('lenght, data', parametrize)
def test_get_all(movie_service, lenght, data):
    """ Тестирование функции get_all() """
    print(lenght, data)
    movie_service.dao.get_all.return_value = data
    test_result = movie_service.get_all()
    assert isinstance(test_result, list)  # проверяем что полученные данные возвращаются списком
    assert len(test_result) == lenght  # проверяем длинну возвращаемого списка
    assert test_result == data  # просто проверка на наличие возвращаемых данных


parametrize = (
    (
        {'id': 1,
         'title': 'first title',
         'description': 'description',
         'trailer': 'trailer',
         'year': 2000,
         'rating': 9, },
        {'id': 1,
         'title': 'change title',
         'description': 'change description',
         'trailer': 'change trailer',
         'year': 2000,
         'rating': 9, },
    ),
)


@pytest.mark.parametrize('original_data, modified_data', parametrize)
def test_partially_update(movie_service, original_data, modified_data):
    """ Тестирование функции partially_update() """
    movie_service.dao.get_one.return_value = original_data
    movie_service.partially_update(modified_data)

    movie_service.dao.get_one.assert_called_once_with(
        original_data['id'])  # assert не пишем, т.к. он уже внутри метода "assert_called_once_with"
    movie_service.dao.update.assert_called_with(
        modified_data)  # assert не пишем, т.к. он уже внутри метода "assert_called_with"


parametrize = (
    (
        {'id': 1,
         'title': 'first title',
         'description': 'description',
         'trailer': 'trailer',
         'year': 2000,
         'rating': 9, },
        {'id': 1,
         'title': 'change title',
         'description': 'change description',
         'trailer': 'change trailer',
         'year': 2000,
         'rating': 9, },
    ),
)


@pytest.mark.parametrize('original_data, modified_data', parametrize)
def test_partially_update_with_wrong_filds(movie_service, original_data, modified_data):
    """ Тестируем функцию  partially_update() на наличие ошибок """
    movie_service.dao.get_one.return_value = original_data

    movie_service.partially_update(modified_data)
    movie_service.dao.update.assert_called_once_with(original_data)


parametrize = (1,)


@pytest.mark.parametrize('movie_id', parametrize)
def test_delete(movie_service, movie_id):
    """ Тестирование функции delete() """
    movie_service.delete(movie_id)
    movie_service.dao.delete.assert_called_once_with(movie_id)


parametrize = (
    (
        {'id': 1,
         'title': mock.ANY,
         'description': mock.ANY,
         'trailer': mock.ANY,
         'year': mock.ANY,
         'rating': mock.ANY, },
    )
)


@pytest.mark.parametrize('movie_data', parametrize)
def test_update(movie_service, movie_data):
    """ Тестирование функции update() """
    movie_service.update(movie_data)
    movie_service.dao.update.assert_called_once_with(movie_data)
