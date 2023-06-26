# You have been hired as a data scientist at a research institute, and your task is to develop a program that analyzes a dataset containing information about patients' medical records. The dataset is represented as a list of dictionaries, where each dictionary represents a patient's record with keys such as 'name', 'age', 'gender', 'diagnosis', and 'treatments'. Your task is to write a Python program that implements the following features:
#
# 1.	Create an empty list to store the patient records.
# 2.	Use a while loop to keep the program running until the user chooses to quit.
# 3.	Display the menu options to the user: "Add patient record", "Search patients", "Analyze data", and "Quit".
# 4.	Use if-else statements to execute the corresponding operation based on the user's choice.
# 5.	For the "Add patient record" option, prompt the user to enter the patient's information and add it as a dictionary to the list of patient records.
# 6.	For the "Search patients" option, prompt the user to enter a search keyword and display the patient records that match the keyword in any of the keys.
# 7.	For the "Analyze data" option, calculate and display the average age of the patients in the dataset.
# 8.	If the user enters an invalid choice, display an error message.
# 9.
# Remember to use list operations and methods, while and for loops, if and else operators, and functions to implement this program.

def display_menu():
    print("Menu Options:")
    print("1. Add patient record")
    print("2. Search patients")
    print("3. Analyze data")
    print("4. Quit")

def add_patient_record(records):
    patient = {}
    patient['name'] = input("Enter patient's name: ")
    patient['age'] = int(input("Enter patient's age: "))
    patient['gender'] = input("Enter patient's gender: ")
    patient['diagnosis'] = input("Enter patient's diagnosis: ")
    patient['treatments'] = input("Enter patient's treatments: ")
    records.append(patient)
    print("Patient record added.")

def search_patients(records):
    keyword = input("Enter a search keyword: ")
    matching_records = [record for record in records if
                        any(keyword.lower() in value.lower() for value in record.values())]
    if matching_records:
        print("Matching patient records:")
    for record in matching_records:
        print(record)
    else:
        print("No patient records found.")

def analyze_data(records):
    total_age = sum(record['age'] for record in records)
    if len(records) > 0:
        average_age = total_age / len(records)
    print(f"Average patient age: {average_age:.2f}")
    else:
    print("No patient records available for analysis.")


patient_records = []
choice = 0

while choice != 4:
    display_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_patient_record(patient_records)
    elif choice == 2:
        search_patients(patient_records)
    elif choice == 3:
        analyze_data(patient_records)
    elif choice == 4:
        print("Thank you for using the patient record analysis program. Goodbye!")
    else:
        print("Invalid choice. Please try again.")
print("Program exited.")
