# You are a teacher managing a class of students. Your task is to keep track of students who have submitted their assignments. You will create a program that allows you to perform set operations on the students' submission status. The program should have the following functionalities:
#
# •	Add students to the set of submissions.
# •	Remove students from the set of submissions.
# •	Check if a student has submitted their assignment.
# •	Count the number of students who have submitted their assignments.
# •	Display the list of students who have not submitted their assignments.
#
# To accomplish this, you need to create a menu-driven program that provides options to perform these operations. The program should continue executing until the user chooses to exit.

def add_student(submissions, student):
    submissions.add(student)
    print(f"Student '{student}' added to the submissions set.")


def remove_student(submissions, student):
    if student in submissions:
        submissions.remove(student)
        print(f"Student '{student}' removed from the submissions set.")
    else:
        print(f"Student '{student}' is not in the submissions set.")


def check_submission_status(submissions, student):
    if student in submissions:
        print(f"Student '{student}' has submitted their assignment.")
    else:
        print(f"Student '{student}' has not submitted their assignment.")


def count_submitted_students(submissions):
    count = len(submissions)
    print(f"Number of students who have submitted their assignments: {count}")


def display_missing_students(submissions, all_students):
    missing_students = all_students - submissions
    if missing_students:
        print("Students who have not submitted their assignments:")
    for student in missing_students:
        print(student)
    else:
        print("All students have submitted their assignments.")


def main():
    submissions = set()
    all_students = set()
    while True:
        print("\nStudent Assignment Management Menu:")
        print("1. Add student to submissions")
        print("2. Remove student from submissions")
        print("3. Check submission status of a student")
        print("4. Count submitted students")
        print("5. Display missing students")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student = input("Enter the student's name: ")
            add_student(submissions, student)
            all_students.add(student)
        elif choice == "2":
            student = input("Enter the student's name: ")
            remove_student(submissions, student)
        elif choice == "3":
            student = input("Enter the student's name: ")
            check_submission_status(submissions, student)
        elif choice == "4":
            count_submitted_students(submissions)
        elif choice == "5":
            display_missing_students(submissions, all_students)
        elif choice == "6":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
