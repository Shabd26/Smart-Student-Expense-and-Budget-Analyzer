import unittest
import tempfile
import os

from modules import expense_manager


class ExpenseTests(unittest.TestCase):

    def setUp(self):
        self.folder = tempfile.mkdtemp()
        self.file = os.path.join(self.folder, "expenses.json")
        self.old_file = expense_manager.EXPENSES_FILE
        expense_manager.EXPENSES_FILE = self.file

    def tearDown(self):
        expense_manager.EXPENSES_FILE = self.old_file

    def test_add_expense(self):
        result = expense_manager.add_expense(100, "Food", "Lunch", "2026-09-20")
        self.assertEqual(result["amount"], 100)
        self.assertEqual(result["category"], "Food")

    def test_view_expenses(self):
        expense_manager.add_expense(100, "Food", "Lunch", "2026-09-20")
        expenses = expense_manager.view_expenses()
        self.assertEqual(len(expenses), 1)

    def test_search_expenses(self):
        expense_manager.add_expense(100, "Food", "Lunch", "2026-09-20")
        expense_manager.add_expense(200, "Study", "Notebook", "2026-09-21")
        result = expense_manager.search_expenses("Lunch")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["category"], "Food")

    def test_filter_expenses(self):
        expense_manager.add_expense(100, "Food", "Lunch", "2026-09-20")
        expense_manager.add_expense(200, "Study", "Notebook", "2026-09-21")
        result = expense_manager.filter_expenses("Study")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["amount"], 200)

    def test_edit_and_delete_expense(self):
        expense_manager.add_expense(100, "Food", "Lunch", "2026-09-20")
        result = expense_manager.edit_expense(1, 150, "Food", "Dinner", "2026-09-22")
        self.assertTrue(result)

        expenses = expense_manager.view_expenses()
        self.assertEqual(expenses[0]["amount"], 150)
        self.assertEqual(expenses[0]["description"], "Dinner")

        result = expense_manager.delete_expense(1)
        self.assertTrue(result)
        self.assertEqual(len(expense_manager.view_expenses()), 0)


if __name__ == "__main__":
    unittest.main()
