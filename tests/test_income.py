import unittest
import tempfile
import os

from modules import income_manager


class IncomeTests(unittest.TestCase):

    def setUp(self):
        self.folder = tempfile.mkdtemp()
        self.file = os.path.join(self.folder, "income.json")
        self.old_file = income_manager.INCOME_FILE
        income_manager.INCOME_FILE = self.file

    def tearDown(self):
        income_manager.INCOME_FILE = self.old_file

    def test_set_income(self):
        result = income_manager.set_income(25000)
        self.assertEqual(result, 25000)

    def test_get_income(self):
        income_manager.set_income(25000)
        result = income_manager.get_income_amount()
        self.assertEqual(result, 25000)


if __name__ == "__main__":
    unittest.main()
