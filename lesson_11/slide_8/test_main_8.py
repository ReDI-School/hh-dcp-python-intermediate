from lesson_11.slide_8.main import validate
import pytest

def test_validate_ok():
    assert validate(1)

def test_validate_exception():
    try:
        validate(-1)
    except ValueError as e:
        assert str(e) == 'Value must be greater than 0'
    else:
        assert False

def test_validate_exception_2():
    with pytest.raises(ValueError) as e:
        validate(-1)
    assert str(e.value) == 'Value must be greater than 0'

