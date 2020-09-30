import unittest
from Employee import *

class TestEmployeeClass(unittest.TestCase):
    """
    Testing class employee
    """
    def setUp(self):
        self.employee = Employee('Alexey', 'Razmanov', 1200)

    def test_give_default_raise(self):
        """
        Testing default giving raise
        """
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 6200)

    def test_give_custom_raise(self):
        """
        Testing custom giving raise
        """
        my_raise = 3000
        self.employee.give_raise(3000)
        self.assertEqual(self.employee.salary, 4200)

unittest.main()