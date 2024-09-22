class Student:
    def __init__(self, name: str, roll_number: int):
        self.__name = name
        self.__roll_number = roll_number
        self.__marks = []

    def add_marks(self, marks: float):
        if 0 <= marks <= 100:
            self.__marks.append(marks)
        else:
            raise ValueError("Marks should be between 0 and 100")

    def calculate_average(self) -> float:
        if not self.__marks:
            return 0.0
        return sum(self.__marks) / len(self.__marks)

    def display_details(self):
        print(f"Name: {self.__name}")
        print(f"Roll Number: {self.__roll_number}")
        print(f"Average Marks: {self.calculate_average()}")

    @property
    def name(self):
        return self.__name

    @property
    def roll_number(self):
        return self.__roll_number

    @property
    def marks(self):
        return self.__marks


class Exam:
    def __init__(self, exam_name: str):
        self.__exam_name = exam_name
        self.__student_marks = {}

    def add_student_marks(self, student: Student, marks: float):
        if 0 <= marks <= 100:
            self.__student_marks[student.roll_number] = marks
            student.add_marks(marks)
        else:
            raise ValueError("Marks should be between 0 and 100")

    def calculate_average_marks(self) -> float:
        if not self.__student_marks:
            return 0.0
        return sum(self.__student_marks.values()) / len(self.__student_marks)

    def display_exam_details(self):
        print(f"Exam Name: {self.__exam_name}")
        print(f"Average Marks: {self.calculate_average_marks()}")

    @property
    def exam_name(self):
        return self.__exam_name

    @property
    def student_marks(self):
        return self.__student_marks


class StudentManagementSystem:
    def __init__(self):
        self.__students: dict[int, Student] = {}
        self.__exams: dict[str, Exam] = {}

    def run(self):
        while True:
            print("\n1. Add Student")
            print("2. Add Exam Marks")
            print("3. Calculate Student Average")
            print("4. Display Student Details")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.add_exam()
            elif choice == '3':
                self.calculate_student_average()
            elif choice == '4':
                self.student_details()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    def calculate_student_average(self):
        roll_number = int(input("Enter student roll number: "))
        if roll_number in self.__students:
            print(f"Average Marks: {self.__students[roll_number].calculate_average()}")
        else:
            print("Student not found")

    def student_details(self):
        roll_number = int(input("Enter student roll number: "))
        if roll_number in self.__students:
            self.__students[roll_number].display_details()
        else:
            print("Student not found")

    def add_student(self):
        name = input("Enter student name: ")
        roll_number = int(input("Enter roll number: "))
        self.__students[roll_number] = Student(name, roll_number)

    def add_exam(self):
        exam_name = input("Enter exam name: ")
        if exam_name not in self.__exams:
            self.__exams[exam_name] = Exam(exam_name)
        roll_number = int(input("Enter student roll number: "))
        if roll_number in self.__students:
            marks = float(input("Enter marks: "))
            try:
                self.__exams[exam_name].add_student_marks(self.__students[roll_number], marks)
            except ValueError as e:
                print(e)
        else:
            print("Student not found")


def main():
    sms = StudentManagementSystem()
    sms.run()


if __name__ == "__main__":
    main()
