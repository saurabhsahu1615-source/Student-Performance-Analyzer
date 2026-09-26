def calculate_total(student):
    total = sum(student["marks"].values())

    return total


def calculate_average(student):
    total = calculate_total(student)

    average = total / len(student["marks"])

    return average


def calculate_grade(average):

    if average >= 90:
        return "A+"

    elif average >= 80:
        return "A"

    elif average >= 70:
        return "B"

    elif average >= 60:
        return "C"

    elif average >= 50:
        return "D"

    else:
        return "F"


def calculate_result(average):

    if average >= 40:
        return "Pass"

    else:
        return "Fail"


def analyze_student(students, find_student):

    student_id = input("Enter Student ID: ")

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

    print("\nPERFORMANCE ANALYSIS")

    print("Student ID:", student["id"])
    print("Name:", student["name"])

    print("\nSubject Marks:")

    for subject, mark in student["marks"].items():
        print(subject, ":", mark)

    print("\nTotal:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)
    print("Result:", result)