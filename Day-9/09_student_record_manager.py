def add_student():
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    course = input("Enter course: ")

    with open("student.txt","a") as file:
        file.write(f"Name:{name}\n")
        file.write(f"Roll Number:{roll_number}\n")
        file.write(f"Course:{course}\n")
        file.write("-------------------------\n")

    print("Student added successfully.")

def view_students():
    with open("student.txt","r") as file:
        data = file.read()

    print("\n========STUDENT RECORDS========")
    print(data)

def search_student():
    name = input("Enter student name to search:")

    with open("student.txt","r") as file:
        data = file.read()

    if name.lower() in data.lower():
        print(f"{name} is present in the records.")
    else:
        print(f"{name} is not present in the records.")

while True:
    print("\n=======STUDENT RECORD MANAGER=======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Thank you for using Student Record Manager.Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")