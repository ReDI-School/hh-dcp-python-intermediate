# Class Design

## Design classes for the following entities: Student, Exam

Each class should have appropriate attributes and methods to represent its properties and behaviors. Implement encapsulation by using appropriate access modifiers for class attributes.

### Student Class

- It Should contain attributes such as student name, roll number, and marks (a list of exam scores).
- Implement methods to calculate the average marks of the student and display their details.

### Exam Class

- It Should represent an exam with attributes like exam name and marks obtained by the students.
- Include methods for adding marks for students and computing average marks for the exam.

## User Interaction

- Implement a simple user interface to interact with the student management system. You can also use a class for it.
- Allow users to add students, add exam marks, calculate student averages, and display student details.

## Error Handling

- Handle potential errors gracefully, such as entering invalid exam marks.

# Example Interaction

```text

1. Add Student
2. Add Exam Marks
3. Calculate Student Average
4. Display Student Details
5. Exit
Enter your choice: 1
Enter student name: Darius
Enter roll number: 1

1. Add Student
2. Add Exam Marks
3. Calculate Student Average
4. Display Student Details
5. Exit
Enter your choice: 2
Enter exam name: IT
Enter student roll number: 1
Enter marks: 95

1. Add Student
2. Add Exam Marks
3. Calculate Student Average
4. Display Student Details
5. Exit
Enter your choice: 3
Enter student roll number: 1
Average Marks: 95.0

1. Add Student
2. Add Exam Marks
3. Calculate Student Average
4. Display Student Details
5. Exit
Enter your choice: 4
Enter student roll number: 1
Name: Darius
Roll Number: 1
Average Marks: 95.0

1. Add Student
2. Add Exam Marks
3. Calculate Student Average
4. Display Student Details
5. Exit
Enter your choice: 5

Process finished with exit code 0

```
