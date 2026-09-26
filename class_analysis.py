from Analysis import*


def class_analysis(students):

    if len(students) == 0:
        print("No students found.")
        return

    students_with_marks = []

    for student in students:
        if len(student["marks"]) > 0:
            students_with_marks.append(student)

    if len(students_with_marks) == 0:
        print("No student marks available.")
        return

    total_average = 0
    highest_student = students_with_marks[0]
    lowest_student = students_with_marks[0]

    grade_distribution = {
        "A+": 0,
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0
    }

    for student in students_with_marks:

        average = calculate_average(student)
        total_average += average

        if average > calculate_average(highest_student):
            highest_student = student

        if average < calculate_average(lowest_student):
            lowest_student = student

        grade = calculate_grade(average)
        grade_distribution[grade] += 1

    class_average = total_average / len(students_with_marks)

    print("\n CLASS ANALYSIS")

    print("Class Average:", round(class_average, 2))

    print("\nHighest Performer:")
    print("ID:", highest_student["id"])
    print("Name:", highest_student["name"])
    print("Average:", round(calculate_average(highest_student), 2))

    print("\nLowest Performer:")
    print("ID:", lowest_student["id"])
    print("Name:", lowest_student["name"])
    print("Average:", round(calculate_average(lowest_student), 2))

    print("\nGrade Distribution:")

    for grade, count in grade_distribution.items():
        print(grade, ":", count)