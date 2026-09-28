class Payroll:
    def __init__(self, employee_id, payroll_month, basic_salary, allowance, deduction):
        self.employee_id = employee_id
        self.payroll_month = payroll_month
        self.basic_salary = basic_salary
        self.allowance = allowance
        self.deduction = deduction

    @property
    def net_salary(self):
        return self.basic_salary + self.allowance - self.deduction
