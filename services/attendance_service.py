from datetime import date
from models.attendance import Attendance


class AttendanceService:
    def __init__(self, db):
        self.db = db

    def mark_attendance_interactive(self):
        employee_id = int(input("Employee ID: "))
        attendance_date = input(
            f"Date (YYYY-MM-DD) [{date.today()}]: "
        ).strip() or str(date.today())

        status = input("Status (Present/Absent/Leave): ").strip().title()
        if status not in {"Present", "Absent", "Leave"}:
            raise ValueError("Status must be Present, Absent, or Leave.")

        attendance = Attendance(employee_id, attendance_date, status)

        query = """
            INSERT INTO attendance (employee_id, attendance_date, status)
            VALUES (%s, %s, %s)
        """
        self.db.execute(
            query,
            (
                attendance.employee_id,
                attendance.attendance_date,
                attendance.status,
            ),
        )
        print("Attendance recorded successfully.")
