# Employee Management & Payroll System

A beginner-friendly software development project built with **Python and MySQL**, demonstrating **OOP, DSA, SQL, CRUD operations, validation, exception handling, and payroll calculation**.

## Skills demonstrated

- Python
- Object-Oriented Programming (OOP)
- MySQL
- SQL CRUD operations
- JOINs and aggregate queries
- Lists and dictionaries
- Linear search and sorting
- Exception handling
- Input validation
- Modular project structure
- Git/GitHub

## Project modules

1. Employee Management
2. Department Management through SQL schema
3. Attendance
4. Payroll
5. Employee search
6. Salary sorting
7. Database connectivity
8. Validation and error handling

## Project structure

```text
employee-management-payroll-system/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── config/
│   └── database_config.py
├── database/
│   └── database.py
├── models/
│   ├── employee.py
│   ├── attendance.py
│   └── payroll.py
├── services/
│   ├── employee_service.py
│   ├── attendance_service.py
│   └── payroll_service.py
├── utils/
│   ├── validation.py
│   └── search_sort.py
├── sql/
│   └── database.sql
└── tests/
    ├── test_validation.py
    └── test_payroll.py
```

## Setup

### 1. Install Python

Python 3.10+ is recommended.

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL

Open `config/database_config.py` and set your MySQL username/password.

Then execute `sql/database.sql` in MySQL Workbench.

### 5. Run

```bash
python main.py
```

## Payroll formula

```text
Net Salary = Basic Salary + Allowance - Deduction
```

This is a simplified learning-project formula and does not represent a company's complete payroll/tax rules.

## Interview explanation

> "I developed an Employee Management and Payroll System using Python and MySQL. I used OOP to separate employee, attendance and payroll responsibilities, MySQL to persist data, SQL JOINs for related information, and DSA concepts such as lists, dictionaries, searching and sorting. I also added validation and exception handling to make the application safer and easier to maintain."

## Important

Do not commit real passwords, API keys, or other secrets to GitHub.
