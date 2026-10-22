
students = []


def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")


def show_students():
    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        print(student["name"], "-", student["marks"])


def show_average():
    if len(students) == 0:
        print("No student records available.")
        return

    total = 0

    for student in students:
        total = total + student["marks"]

    average = total / len(students)
    print("Average marks:", average)


def main():
    while True:
        print("\n--- STUDENT MARKS MANAGER ---")
        print("1. Add student")
        print("2. Show students")
        print("3. Show average marks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            show_average()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
