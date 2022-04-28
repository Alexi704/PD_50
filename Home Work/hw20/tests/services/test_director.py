import pytest
from unittest import mock


class DirectorNotFound(Exception):
    pass


# можно параметры не выносить, а прописывать в фикструре
parametrize = (
    {'id': 1, 'name': 'first name'},
    {'id': 2, 'name': 'second name'},
)


@pytest.mark.parametrize('data', parametrize)
def test_get_one(director_service, data):
    """ Тестирование функции get_one() """
    director_service.dao.get_one.return_value = data

    assert director_service.get_one(data['id']) == data


def test_get_one_with_error(director_service):
    """ Тестируем функцию  get_one() на наличие ошибки в передаваемом id """
    director_service.dao.get_one.side_effect = DirectorNotFound
    with pytest.raises(DirectorNotFound):
        director_service.get_one(0)
        director_service.get_one(-1)
        director_service.get_one(1.5)
        director_service.get_one('any_str')


parametrize = (
    (2, [{'id': 1, 'name': 'first name'}, {'id': 2, 'name': 'second name'}, ],),
    (0, [],),
)


@pytest.mark.parametrize('lenght, data', parametrize)
def test_get_all(director_service, lenght, data):
    """ Тестирование функции get_all() """
    print(lenght, data)
    director_service.dao.get_all.return_value = data
    test_result = director_service.get_all()
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
def test_partially_update(director_service, original_data, modified_data):
    """ Тестирование функции partially_update() """
    director_service.dao.get_one.return_value = original_data
    director_service.partially_update(modified_data)

    director_service.dao.get_one.assert_called_once_with(
        original_data['id'])  # assert не пишем, т.к. он уже внутри метода "assert_called_once_with"
    director_service.dao.update.assert_called_with(
        modified_data)  # assert не пишем, т.к. он уже внутри метода "assert_called_with"


parametrize = (
    (
        {'id': 1, 'name': 'first name'},
        {'id': 1, 'wrong_field': 'wrong_data'},
    ),
)


@pytest.mark.parametrize('original_data, modified_data', parametrize)
def test_partially_update_with_wrong_filds(director_service, original_data, modified_data):
    """ Тестируем функцию  partially_update() на наличие ошибок """
    director_service.dao.get_one.return_value = original_data

    director_service.partially_update(modified_data)
    director_service.dao.update.assert_called_once_with(original_data)


parametrize = (1,)


@pytest.mark.parametrize('director_id', parametrize)
def test_delete(director_service, director_id):
    """ Тестирование функции delete() """
    director_service.delete(director_id)
    director_service.dao.delete.assert_called_once_with(director_id)


parametrize = (
    (
        {
            'id': mock.ANY,
            'name': mock.ANY
        },
    )
)


@pytest.mark.parametrize('director_data', parametrize)
def test_update(director_service, director_data):
    """ Тестирование функции update() """
    director_service.update(director_data)
    director_service.dao.update.assert_called_once_with(director_data)
