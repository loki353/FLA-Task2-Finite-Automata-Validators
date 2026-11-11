import unittest
from validators import validate_pin, validate_password, validate_email

class ValidatorTests(unittest.TestCase):
    def test_pin(self):
        self.assertTrue(validate_pin("1234"))
        self.assertFalse(validate_pin("123"))
        self.assertFalse(validate_pin("12a4"))
        self.assertFalse(validate_pin("12345"))

    def test_password(self):
        self.assertTrue(validate_password("Abcd@123"))
        self.assertFalse(validate_password("abcdefg"))
        self.assertFalse(validate_password("ABCDEFG1"))

    def test_email(self):
        self.assertTrue(validate_email("student@example.com"))
        self.assertFalse(validate_email("student@"))
        self.assertFalse(validate_email("student.example.com"))
        self.assertFalse(validate_email("a..b@example.com"))

if __name__ == "__main__":
    unittest.main()
