import unittest
from validators import validate_mobile, validate_username, validate_time


class ValidatorTests(unittest.TestCase):
    def test_mobile_accepted(self):
        for value in ["9123456780", "6789012345", "7890123456", "8456123097", "9012345678"]:
            self.assertTrue(validate_mobile(value))

    def test_mobile_rejected(self):
        for value in ["5123456789", "612345678", "78901234567", "84561A3097", "3456789012"]:
            self.assertFalse(validate_mobile(value))

    def test_username_accepted(self):
        for value in ["lokesh25", "arjun_24", "priya_2026", "tech_user7", "student99"]:
            self.assertTrue(validate_username(value))

    def test_username_rejected(self):
        for value in ["25lokesh", "_arjun", "priya_", "tech__user", "student@99"]:
            self.assertFalse(validate_username(value))

    def test_time_accepted(self):
        for value in ["06:25", "08:50", "14:35", "17:40", "22:15"]:
            self.assertTrue(validate_time(value))

    def test_time_rejected(self):
        for value in ["25:10", "16:75", "7:45", "20:90", "26:30"]:
            self.assertFalse(validate_time(value))


if __name__ == "__main__":
    unittest.main()
