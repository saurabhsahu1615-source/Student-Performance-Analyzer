SUBJECTS = ["CSE", "Calculus", "English", "EVS"]


def enter_marks(students, find_student):
    student_id = input("Enter Student ID: ")

    student = find_student(students, student_id)

    if student is None:
        print("Student not found!")
        return

    marks = {}

    print("\nEnter marks out of 100:")

    for subject in SUBJECTS:

        while True:
            try:
                mark = int(input(f"Enter marks for {subject}: "))

                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    student["marks"] = marks

    print("Marks entered successfully!")