
# Lab Exercise 2: Student Record Management System

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    marks = input("Enter Marks: ")

    with open("students.txt", "a") as file:
        file.write(roll + "," + name + "," + marks + "\n")

    print("Student added successfully!")


def display_students():
    try:
        with open("students.txt", "r") as file:
            records = file.readlines()

        if not records:
            print("No student records found.")
        else:
            print("\nStudent Records:")
            for record in records:
                roll, name, marks = record.strip().split(",")
                print("Roll Number:", roll)
                print("Name:", name)
                print("Marks:", marks)
                print("--------------------")

    except FileNotFoundError:
        print("No student records found.")


while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        print("Program exited.")
        break
    else:
        print("Invalid choice!")
