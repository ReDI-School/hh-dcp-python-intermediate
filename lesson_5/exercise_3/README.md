# Exercise 3

We will now use our previously created classes to generate a list of random numbers and calculate the min, max and average of this list.

1. Create an instance of the `RandomNumberGenerator` class with the following parameters:
   * n = 10
   * min = 0
   * max = 15
   * Generate a list of random numbers with the `generate_numbers` method.
   * Create an instance of the `NumberStats` class with the generated list.
   * Print the dictionary returned by the `all` method of the `NumberStats` class.

    The output should look like this:
    
    ```python
    {'min': 0, 'max': 15, 'average': 7.5}
    ```

1. Create another instance of the `RandomNumberGenerator` class with the following parameters:
   * n = 5
   * min = 10
   * max = 20
   * Generate a list of random numbers with the `generate_numbers` method.
   * **DON'T** create an new instance of the `NumberStats` class with the generated list.
   * Print the dictionary returned by the `all` method of the `NumberStats` class.
   * Explain why the numbers have not changed.

1. Fix the numbers by creating a new instance of the `NumberStats` class with the new list of numbers.
   * Print the dictionary returned by the `all` method of the `NumberStats` class.

    The output should look like this:
    
    ```python
    {'min': 10, 'max': 20, 'average': 15.0}
    ```

You can find a template for the classes in the [lesson_4/exercise_3/main.py](lesson_4/exercise_3/main.py) file.