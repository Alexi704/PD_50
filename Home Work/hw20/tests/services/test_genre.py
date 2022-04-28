import pytest
from unittest import mock


class GenreNotFound(Exception):
    pass



# можно параметры не выносить, а прописывать в фикструре
parametrize = (
    {'id': 1, 'name': 'first name'},
    {'id': 2, 'name': 'second name'},
)


@pytest.mark.parametrize('data', parametrize)
def test_get_one(genre_service, data):
    """ Тестирование функции get_one() """
    genre_service.dao.get_one.return_value = data

    assert genre_service.get_one(data['id']) == data


def test_get_one_with_error(genre_service):
    """ Тестируем функцию  get_one() на наличие ошибки в передаваемом id """
    genre_service.dao.get_one.side_effect = GenreNotFound
    with pytest.raises(GenreNotFound):
        genre_service.get_one(0)
        genre_service.get_one(-1)
        genre_service.get_one(1.5)
        genre_service.get_one('any_str')


parametrize = (
    (2, [{'id': 1, 'name': 'first name'}, {'id': 2, 'name': 'second name'}, ],),
    (0, [],),
)


@pytest.mark.parametrize('lenght, data', parametrize)
def test_get_all(genre_service, lenght, data):
    """ Тестирование функции get_all() """
    print(lenght, data)
    genre_service.dao.get_all.return_value = data
    test_result = genre_service.get_all()
    assert isinstance(test_result, list)  # проверяем что полученные данные возвращаются списком
    assert len(test_result) == lenght  # проверяем длинну возвращаемого списка
    assert test_result == data  # просто проверка на наличие возвращаемых данных


parametrize = (
    (
        {'id': 1, 'name': 'first name'},
        {'id': 1, 'name': 'change_name'},
    ),
)


@pytest.mark.parametrize('original_data, modified_data', parametrize)
def test_partially_update(genre_service, original_data, modified_data):
    """ Тестирование функции partially_update() """
    genre_service.dao.get_one.return_value = original_data
    genre_service.partially_update(modified_data)

    genre_service.dao.get_one.assert_called_once_with(
        original_data['id'])  # assert не пишем, т.к. он уже внутри метода "assert_called_once_with"
    genre_service.dao.update.assert_called_with(
        modified_data)  # assert не пишем, т.к. он уже внутри метода "assert_called_with"


parametrize = (
    (
        {'id': 1, 'name': 'first name'},
        {'id': 1, 'wrong_field': 'wrong_data'},
    ),
)


@pytest.mark.parametrize('original_data, modified_data', parametrize)
def test_partially_update_with_wrong_filds(genre_service, original_data, modified_data):
    """ Тестируем функцию  partially_update() на наличие ошибок """
    genre_service.dao.get_one.return_value = original_data

    genre_service.partially_update(modified_data)
    genre_service.dao.update.assert_called_once_with(original_data)


parametrize = (1,)


@pytest.mark.parametrize('genre_id', parametrize)
def test_delete(genre_service, genre_id):
    """ Тестирование функции delete() """
    genre_service.delete(genre_id)
    genre_service.dao.delete.assert_called_once_with(genre_id)



parametrize = (
    (
        {
            'id': mock.ANY,
            'name': mock.ANY
        },
    )
)


@pytest.mark.parametrize('genre_data', parametrize)
def test_update(genre_service, genre_data):
    """ Тестирование функции update() """
    genre_service.update(genre_data)
    genre_service.dao.update.assert_called_once_with(genre_data)
