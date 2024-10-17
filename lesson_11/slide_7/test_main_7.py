import pytest

from lesson_11.slide_7.main import run

def test_run():
    duration, words = run()
    assert words == 95
    assert duration == pytest.approx(1.0, 0.5)

