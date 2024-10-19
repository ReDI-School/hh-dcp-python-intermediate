# Exercise 1
From lesson 2, exercise 1, you create a program for grade calculation. 
You need to add tests to it, ensuring it works as expected.
It may be required to refactor the code to make it testable.

Here is the solution code for the exercise:

```python
class GradeCalculator:
    def calculate_grade(self, marks: int) -> str:
        if 90 <= marks <= 100:
            return "A"
        elif 80 <= marks <= 89:
            return "B"
        elif 70 <= marks <= 79:
            return "C"
        elif 60 <= marks <= 69:
            return "D"
        elif 0 <= marks <= 59:
            return "F"
        else:
            return "Invalid marks"
```
* Your test should cover all the conditions in the `calculate_grade` method.
* Also think about edges, like calculating negative marks.
* And play around if you add something as mark, that is not an integer (for example a string, a list or a tuple).
* You can refactor and extend the code to make it testable if needed.