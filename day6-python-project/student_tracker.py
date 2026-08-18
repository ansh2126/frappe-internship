import json

FILE_NAME = "students.json"


def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "marks": marks
    }

    students.append(student)
    save_students(students)

    print("Student added successfully.")


def show_students(students):
    if not students:
        print("No students found.")
        return

    print("\n--- Student Marks ---")

    for student in students:
        print(f"Name: {student['name']} | Marks: {student['marks']}")


def show_average(students):
    if not students:
        print("No marks available.")
        return

    total = sum(student["marks"] for student in students)
    average = total / len(students)

    print(f"Average Marks: {average:.2f}")


def main():
    students = load_students()

    while True:
        print("\n--- Student Marks Tracker ---")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Show Average")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            show_students(students)

        elif choice == "3":
            show_average(students)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
