import unittest
import tempfile
import os

from modules import budget_manager
from modules import expense_manager


class BudgetTests(unittest.TestCase):

    def setUp(self):
        self.folder = tempfile.mkdtemp()
        self.budget_file = os.path.join(self.folder, "budget.json")
        self.expense_file = os.path.join(self.folder, "expenses.json")

        self.old_budget = budget_manager.BUDGET_FILE
        self.old_expenses = expense_manager.EXPENSES_FILE

        budget_manager.BUDGET_FILE = self.budget_file
        expense_manager.EXPENSES_FILE = self.expense_file

    def tearDown(self):
        budget_manager.BUDGET_FILE = self.old_budget
        expense_manager.EXPENSES_FILE = self.old_expenses

    def test_set_monthly_budget(self):
        result = budget_manager.set_monthly_budget(5000)
        self.assertEqual(result, 5000)
        self.assertEqual(budget_manager.get_budget()["monthly_budget"], 5000)

    def test_set_category_budget(self):
        budget_manager.set_category_budget("Food", 1000)
        budget = budget_manager.get_budget()
        self.assertEqual(budget["category_budgets"]["Food"], 1000)

    def test_budget_within_limit(self):
        budget_manager.set_monthly_budget(500)
        expense_manager.add_expense(100, "Food", "Lunch", "2026-09-20")

        result = budget_manager.get_budget_status()

        self.assertEqual(result["overall"]["spent"], 100)
        self.assertEqual(result["overall"]["remaining"], 400)
        self.assertEqual(result["overall"]["status"], "within limit")

    def test_budget_exceeded(self):
        budget_manager.set_monthly_budget(100)
        expense_manager.add_expense(150, "Food", "Lunch", "2026-09-20")

        result = budget_manager.get_budget_status()

        self.assertEqual(result["overall"]["spent"], 150)
        self.assertEqual(result["overall"]["status"], "exceeded")


if __name__ == "__main__":
    unittest.main()
