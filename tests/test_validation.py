import unittest
from utils.validation import validate_email, validate_positive_number, validate_required


class TestValidation(unittest.TestCase):
    def test_required(self):
        self.assertEqual(validate_required(" David "), "David")

    def test_email(self):
        self.assertTrue(validate_email("david@example.com"))
        self.assertFalse(validate_email("invalid-email"))

    def test_positive_number(self):
        self.assertEqual(validate_positive_number("1000"), 1000.0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            validate_positive_number("-1")


if __name__ == "__main__":
    unittest.main()
