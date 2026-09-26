from Analysis import*
from marks import SUBJECTS


def generate_report(students, find_student):

    student_id = input("Enter Student ID for report: ")

    student = find_student(students, student_id)

    if student is None:
        print("Student not found!")
        return

    if len(student["marks"]) == 0:
        print("Marks have not been entered for this student.")
        return

    total = calculate_total(student)
    average = calculate_average(student)
    grade = calculate_grade(average)
    result = calculate_result(average)

    print()
    print("STUDENT REPORT")
    print()

    print("Student ID:", student["id"])
    print("Student Name:", student["name"])

    print("\nSubject Marks:")

    for subject in SUBJECTS:
        print(subject, ":", student["marks"][subject])

    print("\nTotal Marks:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)
    print("Result:", result)

    print()