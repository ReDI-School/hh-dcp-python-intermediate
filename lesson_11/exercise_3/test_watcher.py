import unittest
from unittest.mock import patch, MagicMock
import os

@patch('os.listdir')
@patch('builtins.print')
def test_watch_directory(print_mock, listdir_mock):
    # Initial state: no files
    listdir_mock.side_effect = [
        [],  # First call: no files
        ['new_file.txt']  # Second call: new file appears
    ]

    from lesson_11.exercise_3.main import watch_directory

    # To stop the infinite loop after the first iteration
    with patch('time.sleep', side_effect=StopIteration):
        try:
            watch_directory("/path/to/directory")
        except StopIteration:
            pass

    print_mock.assert_any_call("Watching directory: /path/to/directory")
    print_mock.assert_any_call("New file created: new_file.txt")

if __name__ == "__main__":
    unittest.main()