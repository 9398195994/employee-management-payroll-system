class Employee:
    def __init__(self, name, email, phone, department_id, designation, joining_date, salary):
        self.name = name
        self.email = email
        self.phone = phone
        self.department_id = department_id
        self.designation = designation
        self.joining_date = joining_date
        self.salary = salary

    def __str__(self):
        return f"{self.name} | {self.designation} | ₹{self.salary:.2f}"
