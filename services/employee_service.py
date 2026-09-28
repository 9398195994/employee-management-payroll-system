from datetime import date
from models.employee import Employee
from utils.search_sort import linear_search, sort_by_salary
from utils.validation import (
    validate_email,
    validate_positive_number,
    validate_required,
)


class EmployeeService:
    def __init__(self, db):
        self.db = db

    def add_employee_interactive(self):
        name = validate_required(input("Name: "))
        email = input("Email: ").strip()
        if not validate_email(email):
            raise ValueError("Invalid email address.")

        phone = validate_required(input("Phone: "))
        department_id = int(input("Department ID: "))
        designation = validate_required(input("Designation: "))
        joining_date = input("Joining date (YYYY-MM-DD): ").strip() or str(date.today())
        salary = validate_positive_number(input("Salary: "))

        employee = Employee(
            name, email, phone, department_id, designation, joining_date, salary
        )

        query = """
            INSERT INTO employees
            (name, email, phone, department_id, designation, joining_date, salary)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        employee_id = self.db.execute(
            query,
            (
                employee.name,
                employee.email,
                employee.phone,
                employee.department_id,
                employee.designation,
                employee.joining_date,
                employee.salary,
            ),
        )
        print(f"Employee added successfully. ID: {employee_id}")

    def list_employees(self):
        query = """
            SELECT e.employee_id, e.name, e.email, e.phone,
                   d.department_name, e.designation, e.joining_date,
                   e.salary, e.status
            FROM employees e
            JOIN departments d ON e.department_id = d.department_id
            ORDER BY e.employee_id
        """
        employees = self.db.execute(query, fetch=True)

        if not employees:
            print("No employees found.")
            return

        print("\nID | Name | Email | Department | Designation | Salary | Status")
        print("-" * 95)
        for e in employees:
            print(
                f"{e['employee_id']} | {e['name']} | {e['email']} | "
                f"{e['department_name']} | {e['designation']} | "
                f"₹{e['salary']:.2f} | {e['status']}"
            )

    def search_employee_interactive(self):
        keyword = input("Enter employee name keyword: ").strip().lower()
        employees = self.db.execute(
            "SELECT employee_id, name, email, designation, salary FROM employees",
            fetch=True,
        )
        results = linear_search(employees, keyword, key=lambda item: item["name"])

        # Demonstrates sorting after searching.
        results = sort_by_salary(results, descending=True)

        if not results:
            print("No matching employees.")
            return

        for e in results:
            print(
                f"ID: {e['employee_id']} | {e['name']} | "
                f"{e['designation']} | ₹{e['salary']:.2f}"
            )
