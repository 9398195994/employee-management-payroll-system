CREATE DATABASE IF NOT EXISTS employee_db;
USE employee_db;

CREATE TABLE IF NOT EXISTS departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL UNIQUE,
    manager_name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL,
    department_id INT NOT NULL,
    designation VARCHAR(100) NOT NULL,
    joining_date DATE NOT NULL,
    salary DECIMAL(12,2) NOT NULL,
    status ENUM('Active','Inactive') DEFAULT 'Active',
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE IF NOT EXISTS attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT NOT NULL,
    attendance_date DATE NOT NULL,
    status ENUM('Present','Absent','Leave') NOT NULL,
    UNIQUE KEY unique_employee_date (employee_id, attendance_date),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

CREATE TABLE IF NOT EXISTS payroll (
    payroll_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT NOT NULL,
    payroll_month CHAR(7) NOT NULL,
    basic_salary DECIMAL(12,2) NOT NULL,
    allowance DECIMAL(12,2) NOT NULL DEFAULT 0,
    deduction DECIMAL(12,2) NOT NULL DEFAULT 0,
    net_salary DECIMAL(12,2) NOT NULL,
    UNIQUE KEY unique_employee_month (employee_id, payroll_month),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

INSERT IGNORE INTO departments (department_name, manager_name)
VALUES
('Engineering', 'Arun Kumar'),
('Human Resources', 'Priya Sharma'),
('Finance', 'Rahul Reddy'),
('IT', 'Kiran Rao');

-- Example JOIN query
SELECT e.employee_id, e.name, d.department_name, e.designation, e.salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

-- Example aggregate query
SELECT d.department_name, COUNT(*) AS employee_count, AVG(e.salary) AS average_salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_id, d.department_name;
