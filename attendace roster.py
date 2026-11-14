students = {}


def attendance():
    name = input("Enter student name: ")

    status = input("Enter P for Present or A for Absent: ").upper()

    if status == "P":
        students[name] = "Present"
        print(name, "is marked Present")

    elif status == "A":
        students[name] = "Absent"
        print(name, "is marked Absent")

    else:
        print("Enter only P or A")


def display():
    print("\n--- Student Attendance ---")

    if len(students) == 0:
        print("No attendance marked yet.")

    else:
        for name, status in students.items():
            print(name, "-", status)


# Main program
while True:

    print("\n1. Mark Attendance")
    print("2. Display Attendance")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        attendance()

    elif choice == "2":
        display()

    elif choice == "3":
        print("Program closed.")
        break

    else:
        print("Invalid choice")