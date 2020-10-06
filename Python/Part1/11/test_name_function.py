import unittest
from name_function import get_fomatted_name

class NamesTestCase(unittest.TestCase):
    """Тесты для 'name_function.py'"""

    def test_first_last_name(self):
        """Имена вида 'Janis Joplin' работают правильно?"""
        formatted_name = get_fomatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
        """Имена вида 'Алексей Сергеевич Разманов' работают правильно?"""
        formatted_name = get_fomatted_name('алексей', 'разманов', 'сергеевич')
        self.assertEqual(formatted_name, 'Алексей Сергеевич Разманов')

unittest.main()