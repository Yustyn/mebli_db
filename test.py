import unittest
from methods import Admin, SuperAdmin


class SuperAdminTests(unittest.TestCase):
    # valid data
    VALID_EMAIL = 'Correct@email.com'
    VALID_PASSWORD = 'AQwe12!_'
    # invalid data
    # INVALID_INIT = ('Incorrect@email.com', 12345678,)
    INVALID_EMAIL = 'Incorrect@@email..com'
    INVALID_PASSWORD = 12345678

    def setUp(self):

        #     # create SuperAdmin
        #     self.admin = SuperAdmin(self.VALID_EMAIL, self.VALID_PASSWORD)
        pass

    def test_create_SuperAdmin(self):
        # Test valid data
        super_admin_valid = SuperAdmin(self.VALID_EMAIL, self.VALID_PASSWORD)
        self.assertIsInstance(super_admin_valid, SuperAdmin)
        print('Test 1.1: passed')

    def test_create_invalid_email_SuperAdmin(self):
        # Test invalid data
        super_admin_invalid = SuperAdmin(
            self.INVALID_EMAIL, self.INVALID_PASSWORD)
        self.assertIsInstance(self.INVALID_EMAIL, str)
        print('Test 1.2: passed')

    def test_create_invalid_password_SuperAdmin(self):
        super_admin_invalid = SuperAdmin(
            self.INVALID_EMAIL, self.INVALID_PASSWORD)
        self.assertIsInstance(self.INVALID_PASSWORD, str)
        print('Test 1.3: passed')

    def test_create_invalid_SuperAdmin(self):
        super_admin_invalid = SuperAdmin(
            self.INVALID_EMAIL, self.INVALID_PASSWORD)
        self.assertIsInstance(super_admin_invalid, SuperAdmin,)
        print('Test 1.4: passed')


if __name__ == '__main__':
    unittest.main()
