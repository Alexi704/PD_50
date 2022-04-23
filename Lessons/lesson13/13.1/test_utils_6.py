import pytest

from utils_6 import get_period


grade_parameters = [
    (6, "ночь"),
    (10, "утро"),
    (17, "день"),
    (18, "вечер"),
]

@pytest.mark.parametrize("grade_int, grade_str", grade_parameters)
def test_get_verbal_grade(grade_int, grade_str):
    assert get_period(grade_int) == grade_str


grade_exceptions = [
    (-1, ValueError),
    (25, ValueError),
    ("5", TypeError),
    (5.0, TypeError)
]


@pytest.mark.parametrize("grade_int, exception", grade_exceptions)
def test_get_verbal_grade_exceptions(grade_int, exception):
    with pytest.raises(exception):
        assert get_period(grade_int)
