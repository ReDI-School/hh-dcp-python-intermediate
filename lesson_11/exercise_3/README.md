# Exercise 3

We want to build a simple file watcher in python.
We want to watch a directory and print a message when a file is created.

A file watcher can be implemented using a python script that runs in a loop and checks the directory for new files.
* Loop through the files in the directory of your choice. You can use the `os.listdir()` function to get a list of files in the directory.
* Check if the file is new by comparing it against a list of files that you have already seen.
* Print a message if the file is new

You can use the `time.sleep()` function to pause the script for a few seconds between each iteration of the loop.
You can test your file watcher by creating a new file in the directory that you are watching. 
You may use the `touch` command to create a new file in the terminal.

On Linux or MacOS
```bash
touch /path/to/directory/new_file.txt
```

or on Windows

```cmd
echo. 2> /path/to/directory/new_file.txt
```

Writing tests for this script can be challenging because it involves interacting with the filesystem.
You can use the `unittest.mock` module to mock the filesystem functions as we discussed and test the behavior of the script.
Your test should look into a directory, see no files, then loop again and see a file, then print a message.
As print have no result, you can use the `unittest.mock` module to mock the `print` function and check if it was called with the expected message.

The following mock may help you to test the script:

```python
from unittest.mock import patch

@patch('builtins.print')
def test_file_watcher(print_mock):
    # Your test code here
    pass
    print_mock.assert_called_with("New file created: new_file.txt")
```

And you can use side_effect to have different results in the mock:

```python
from unittest.mock import patch


@patch('os.listdir')
def test_file_watcher_2(listdir_mock):
    listdir_mock.side_effect = [['file1.txt'], ['file1.txt', 'file2.txt']]
    # Your test code here
    pass
```

You also have the problem that your script will run in an infinite loop.
You have to catch `StopIteration` Exception to break the loop and stop the test when all mock calls are processed.