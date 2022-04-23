import pytest


def pytest_make_parametrize_id(config, val):
    """ корректное отображение в терминале кодировки UTF-8 """
    return repr(val)


@pytest.fixture()
def two_numbers_sum():
    return (1, 1, 2)
