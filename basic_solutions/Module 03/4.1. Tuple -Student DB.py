# In this exercise, we will work with tuple operations and methods to create a program that manages a student database. We will use tuples to store the student information and perform various operations on the student records.
#
# Your task is to write the code that allows the user to perform the following operations on a student database:
# •	Add a new student record.
# •	Display all student records.
# •	Search for a student by name.
# •	Update a student's grade.
# •	Remove a student record.
#
# Once you have completed the code, test it by performing the specified operations on the student database.

# Initialize an empty student database
student_database = []

while True:
    print("Menu:")
    print("1. Add new student record")
    print("2. Display all student records")
    print("3. Search student by name")
    print("4. Update student grade")
    print("5. Remove student record")
    print("6. Quit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        student_record = (name, grade)
        student_database.append(student_record)
        print("Student record added.")

    elif choice == "2":
        print("Student Records:")
        if len(student_database) == 0:
            print("No student records found.")
        else:
            for record in student_database:
                name, grade = record
                print(f"Name: {name}, Grade: {grade}")

    elif choice == "3":
        search_name = input("Enter the name to search: ")
        found = False
        for record in student_database:
            name, grade = record
            if name == search_name:
                print("Student found:")
                print(f"Name: {name}, Grade: {grade}")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "4":
        update_name = input("Enter the name of the student to update: ")
        found = False
        for i, record in enumerate(student_database):
            name, grade = record
            if name == update_name:
                new_grade = input("Enter the new grade: ")
                student_database[i] = (name, new_grade)
                print("Student grade updated.")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "5":
        remove_name = input("Enter the name of the student to remove: ")
        found = False
        for record in student_database:
            name, grade = record
            if name == remove_name:
                student_database.remove(record)
                print("Student record removed.")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "6":
        print("Thank you for using the student database manager!")
        break

    else:
        print("Invalid choice. Please try again.")
