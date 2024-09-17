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

grade_calculator = GradeCalculator()
print(grade_calculator.calculate_grade(95)) # Output: A
print(grade_calculator.calculate_grade(25)) # Output: F
print(grade_calculator.calculate_grade(-100)) # Output: Invalid marks