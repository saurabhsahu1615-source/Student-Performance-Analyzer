
from student import*
from marks import*
from Analysis import*
from class_analysis import*
from report import*

students = []

#MAIN FUNCTION
def main():

    while True:

        print("\n")
        print()
        print("STUDENT PERFORMANCE ANALYZER")
        print()

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Enter / Update Marks")
        print("6. Analyze Student Performance")
        print("7. Class Analysis")
        print("8. Generate Student Report")
        print("9. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            enter_marks(students, find_student)

        elif choice == "6":
            analyze_student(students, find_student)

        elif choice == "7":
            class_analysis(students)

        elif choice == "8":
            generate_report(students, find_student)

        elif choice == "9":
            print("Thank you for using Student Performance Analyzer!")
            break

        else:
            print("Invalid choice. Please try again.")

main()