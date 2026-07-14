#=========================================

# Assignment: Student Management System
# Author: Muhammad Ahtsham Javed
# Language: Python
# version: 1.0

#=========================================

class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.__grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
            print(f"Grade {grade} added for {self.name}.")
        else:
            print("Grade must be between 0 and 100.")

    def get_average_grade(self):
        if not self.__grades:
            return 0
        return sum(self.__grades) / len(self.__grades)

    def display_student_info(self):
        print("Student Information:")
        print(f"\tStudent ID: {self.student_id}")
        print(f"\tName: {self.name}")
        print(f"\tAge: {self.age}")
        print(f"\tAverage Grade: {self.get_average_grade():.2f}")


def add_student(students):
    student_id = input("Enter student ID: ").strip()
    if student_id in students:
        print("A student with that ID already exists.")
        return

    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        age = int(input("Enter student age: ").strip())
        if age <= 0:
            raise ValueError
    except ValueError:
        print("Age must be a positive integer.")
        return

    students[student_id] = Student(student_id, name, age)
    print(f"Student {name} added successfully.")


def remove_student(students):
    student_id = input("Enter student ID to remove: ").strip()
    if student_id in students:
        removed_name = students[student_id].name
        del students[student_id]
        print(f"Student {removed_name} removed successfully.")
    else:
        print("No student found with that ID.")


def add_grade_to_student(students):
    student_id = input("Enter student ID: ").strip()
    student = students.get(student_id)
    if not student:
        print("No student found with that ID.")
        return

    try:
        grade = float(input("Enter grade (0-100): ").strip())
    except ValueError:
        print("Grade must be a number.")
        return

    student.add_grade(grade)


def display_student(students):
    student_id = input("Enter student ID: ").strip()
    student = students.get(student_id)
    if student:
        student.display_student_info()
    else:
        print("No student found with that ID.")


def list_students(students):
    if not students:
        print("No students are registered yet.")
        return

    print("Registered Students:")
    for student in students.values():
        average = student.get_average_grade()
        print(f"\t{student.student_id}: {student.name}, Age {student.age}, Avg Grade {average:.2f}")


def display_menu():
    print("\nStudent Management System")
    print("1. Add student")
    print("2. Remove student")
    print("3. Add grade to student")
    print("4. Display student information")
    print("5. List all students")
    print("6. Exit")


def main():
    students = {}
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            remove_student(students)
        elif choice == "3":
            add_grade_to_student(students)
        elif choice == "4":
            display_student(students)
        elif choice == "5":
            list_students(students)
        elif choice == "6":
            print("Exiting the Student Management System. Goodbye!")
            break
        else:
            print("Please choose a valid option from 1 to 6.")


if __name__ == "__main__":
    main()
    