import unittest
from models.payroll import Payroll


class TestPayroll(unittest.TestCase):
    def test_net_salary(self):
        payroll = Payroll(1, "2026-09", 30000, 5000, 2000)
        self.assertEqual(payroll.net_salary, 33000)

    def test_zero_allowance_and_deduction(self):
        payroll = Payroll(1, "2026-09", 30000, 0, 0)
        self.assertEqual(payroll.net_salary, 30000)


if __name__ == "__main__":
    unittest.main()
