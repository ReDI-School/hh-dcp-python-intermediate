class GradeCalculator:
    def calculate_grade(self, marks: int) -> str:
        if not isinstance(marks, int):
            return "Invalid marks"
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