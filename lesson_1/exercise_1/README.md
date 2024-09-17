# Class Exercise 1: Let’s write code!

Create a Python class called `GradeCalculator` that calculates the grade of a student based on their marks. 
The class should have the following method:
* `calculate_grade(marks: int) -> str`: This method should take an integer as input and return a string representing the grade of the student. The grade should be calculated as follows:
  * 90-100: A
  * 80-89: B
  * 70-79: C
  * 60-69: D
  * 0-59: F

Open `lesson 1/exercise 1/main.py` and extend it with your solution. 
You can execute the code or look into the `lesson 1/exercise 1solution.py` file to see the correct answer.

In case your marks are not in the range of 0-100, the method should return `Invalid marks`.

## Example usage
```python

grade_calculator = GradeCalculator()
print(grade_calculator.calculate_grade(95)) # Output: A
print(grade_calculator.calculate_grade(-100)) # Output: Invalid marks
```