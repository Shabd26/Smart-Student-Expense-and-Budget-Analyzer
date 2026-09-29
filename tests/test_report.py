import unittest
import tempfile
import os

from modules import expense_manager
from modules import income_manager
from modules import budget_manager
from modules import goal_manager
from modules import report_generator


class ReportTests(unittest.TestCase):

    def setUp(self):
        self.folder = tempfile.mkdtemp()

        self.expense_file = os.path.join(self.folder, "expenses.json")
        self.income_file = os.path.join(self.folder, "income.json")
        self.budget_file = os.path.join(self.folder, "budget.json")
        self.goals_file = os.path.join(self.folder, "goals.json")

        self.old_expense = expense_manager.EXPENSES_FILE
        self.old_income = income_manager.INCOME_FILE
        self.old_budget = budget_manager.BUDGET_FILE
        self.old_goals = goal_manager.GOALS_FILE

        expense_manager.EXPENSES_FILE = self.expense_file
        income_manager.INCOME_FILE = self.income_file
        budget_manager.BUDGET_FILE = self.budget_file
        goal_manager.GOALS_FILE = self.goals_file

    def tearDown(self):
        expense_manager.EXPENSES_FILE = self.old_expense
        income_manager.INCOME_FILE = self.old_income
        budget_manager.BUDGET_FILE = self.old_budget
        goal_manager.GOALS_FILE = self.old_goals

    def test_generate_report_total(self):
        income_manager.set_income(10000)

        expense_manager.add_expense(500, "Food", "Lunch", "2026-09-20")
        expense_manager.add_expense(1000, "Study", "Book", "2026-09-21")

        budget_manager.set_monthly_budget(5000)

        report = report_generator.generate_report()

        self.assertEqual(report["income"], 10000)
        self.assertEqual(report["total_spending"], 1500)
        self.assertEqual(report["remaining_money"], 8500)

    def test_generate_report_contains_sections(self):
        income_manager.set_income(10000)
        budget_manager.set_monthly_budget(5000)

        report = report_generator.generate_report()

        self.assertIn("income", report)
        self.assertIn("total_spending", report)
        self.assertIn("budget_status", report)
        self.assertIn("goals", report)


if __name__ == "__main__":
    unittest.main()
