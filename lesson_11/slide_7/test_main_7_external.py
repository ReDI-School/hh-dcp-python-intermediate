from unittest.mock import patch
from lesson_11.slide_7.main import run

def fetch_wikipedia():
    return "a " * 95


@patch('wikipedia.summary', return_value=fetch_wikipedia())
def test_run(mock_fetch_wikipedia):
    duration, words = run()
    assert words == 95
    assert duration < 0.0001
    assert mock_fetch_wikipedia.called

