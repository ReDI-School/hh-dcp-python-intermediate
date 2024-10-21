from lesson_11.exercise_1.main import GradeCalculator

instance = GradeCalculator()

def test_grade_calculator():
    assert instance.calculate_grade(95) == 'A'
    assert instance.calculate_grade(85) == 'B'
    assert instance.calculate_grade(75) == 'C'
    assert instance.calculate_grade(65) == 'D'
    assert instance.calculate_grade(55) == 'F'


def test_negative_marks():
    assert instance.calculate_grade(-10) == 'Invalid marks'

def test_invalid_input():
    assert instance.calculate_grade("this is not a number") == 'Invalid marks'
