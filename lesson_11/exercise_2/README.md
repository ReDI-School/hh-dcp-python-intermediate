# Exercise 2
From lesson 2, homework exercise 1, you create a program for some calculations. 
You need to add tests to it, ensuring it works as expected.
It may be required to refactor the code to make it testable.

Here is the solution code for the exercise:

```python
numbers = "13,27,5,67,39,2,10,89,41,7,9,73"

# Split the string into a list of numbers
number_list = numbers.split(',')

# Increase each number by 2
new_number_list = [str(int(num) + 2) for num in number_list]

# Join the list back into a comma-separated string
new_numbers = ','.join(new_number_list)

# Print the result
print(new_numbers)  # Output: 15,29,7,69,41,4,12,91,43,9,11,75

# Alternative solution using list comprehension
print(','.join([str(int(num) + 2) for num in numbers.split(',')]))  # Output: 15,29,7,69,41,4,12,91,43,9,11,75

# Alternative solution using map and lambda
print(','.join(map(lambda x: str(int(x) + 2), numbers.split(','))))  # Output: 15,29,7,69,41,4,12,91,43,9,11,75
```
* Move the code into a function `incrase(my_list: str) -> str` so you can test it.
* Add a test for the function, ensuring it works as expected.
* Test the function with an empty list.
* Test the function with a list of float `incrase("3.5,5.6") -> "5.5,7.6"`. Will it work? If not, how can you fix it?
* In germany, is common to use a comma as decimal separator. 
  Test the function with a list of float using comma as decimal separator `incrase("3,5,5,6") -> "5.5,7.6"`. Will it work? If not, how can you fix it?
* Finally, every test is working under all explained conditions. Refactor the code if needed.
