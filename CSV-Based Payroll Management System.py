
import csv

try:
    n = int(input("Enter number of employees: "))

    with open("payroll.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Employee ID", "Name", "Basic Salary",
            "Allowance", "Deduction", "Net Salary"
        ])

        for i in range(n):
            print("\nEnter details of Employee", i + 1)

            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            basic = float(input("Enter Basic Salary: "))
            allowance = float(input("Enter Allowance: "))
            deduction = float(input("Enter Deduction: "))

            net_salary = basic + allowance - deduction

            writer.writerow([
                emp_id, name, basic,
                allowance, deduction, net_salary
            ])

            print("Net Salary:", net_salary)

    print("\nEmployee Payroll Records:")

    with open("payroll.csv", "r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            print(" | ".join(row))

except ValueError:
    print("Error: Please enter valid numeric values.")

except OSError as e:
    print("File operation error:", e)
