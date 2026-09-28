from models.payroll import Payroll
from utils.validation import validate_positive_number


class PayrollService:
    def __init__(self, db):
        self.db = db

    def generate_payroll_interactive(self):
        employee_id = int(input("Employee ID: "))
        month = input("Payroll month (YYYY-MM): ").strip()
        basic_salary = validate_positive_number(input("Basic salary: "))
        allowance = validate_positive_number(input("Allowance: "))
        deduction = validate_positive_number(input("Deduction: "))

        payroll = Payroll(
            employee_id,
            month,
            basic_salary,
            allowance,
            deduction,
        )

        query = """
            INSERT INTO payroll
            (employee_id, payroll_month, basic_salary, allowance, deduction, net_salary)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.db.execute(
            query,
            (
                payroll.employee_id,
                payroll.payroll_month,
                payroll.basic_salary,
                payroll.allowance,
                payroll.deduction,
                payroll.net_salary,
            ),
        )
        print(f"Payroll generated. Net salary: ₹{payroll.net_salary:.2f}")

    def list_payroll(self):
        query = """
            SELECT p.payroll_id, e.name, p.payroll_month,
                   p.basic_salary, p.allowance, p.deduction, p.net_salary
            FROM payroll p
            JOIN employees e ON p.employee_id = e.employee_id
            ORDER BY p.payroll_month DESC, p.payroll_id DESC
        """
        records = self.db.execute(query, fetch=True)

        if not records:
            print("No payroll records found.")
            return

        for p in records:
            print(
                f"ID: {p['payroll_id']} | {p['name']} | "
                f"{p['payroll_month']} | Basic: ₹{p['basic_salary']:.2f} | "
                f"Allowance: ₹{p['allowance']:.2f} | "
                f"Deduction: ₹{p['deduction']:.2f} | "
                f"Net: ₹{p['net_salary']:.2f}"
            )
