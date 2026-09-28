from services.employee_service import EmployeeService
from services.attendance_service import AttendanceService
from services.payroll_service import PayrollService
from database.database import Database


def menu():
    print("\n===== Employee Management & Payroll System =====")
    print("1. Add employee")
    print("2. List employees")
    print("3. Search employee")
    print("4. Mark attendance")
    print("5. Generate payroll")
    print("6. View payroll")
    print("7. Exit")


def main():
    db = Database()
    employee_service = EmployeeService(db)
    attendance_service = AttendanceService(db)
    payroll_service = PayrollService(db)

    while True:
        menu()
        choice = input("Enter choice: ").strip()

        try:
            if choice == "1":
                employee_service.add_employee_interactive()
            elif choice == "2":
                employee_service.list_employees()
            elif choice == "3":
                employee_service.search_employee_interactive()
            elif choice == "4":
                attendance_service.mark_attendance_interactive()
            elif choice == "5":
                payroll_service.generate_payroll_interactive()
            elif choice == "6":
                payroll_service.list_payroll()
            elif choice == "7":
                print("Thank you. Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1-7.")
        except Exception as exc:
            print(f"Error: {exc}")

    db.close()


if __name__ == "__main__":
    main()
