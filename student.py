def add_student(students):
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Student Name: ")

    student = {
        "id": student_id,
        "name": name,
        "marks": {}
    }

    students.append(student)

    print("Student added successfully!")


def view_students(students):
    if len(students) == 0:
        print("No students found.")
        return

    print("\nSTUDENT LIST")

    for student in students:
        print("ID:", student["id"])
        print("Name:", student["name"])

        if len(student["marks"]) == 0:
            print("Marks: Not entered")
        else:
            print("Marks: Entered")

        print()


def find_student(students, student_id):
    for student in students:
        if student["id"] == student_id:
            return student

    return None


def search_student(students):
    student_id = input("Enter Student ID to search: ")

    student = find_student(students, student_id)

    if student is None:
        print("Student not found!")
        return

    print("\nStudent Found!")
    print("ID:", student["id"])
    print("Name:", student["name"])


def update_student(students):
    student_id = input("Enter Student ID to update: ")

    student = find_student(students, student_id)

    if student is None:
        print("Student not found!")
        return

    new_name = input("Enter new name: ")

    student["name"] = new_name

    print("Student details updated successfully!")