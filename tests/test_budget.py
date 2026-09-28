import unittest


class BudgetTests(unittest.TestCase):

    def test_budget_calculation(self):
        budget = 500
        spending = 100

        remaining = budget - spending

        self.assertEqual(remaining, 400)

    def test_budget_warning(self):
        budget = 500
        spending = 450

        percentage = (spending / budget) * 100

        self.assertTrue(percentage >= 80)

    def test_budget_exceeded(self):
        budget = 100
        spending = 125

        self.assertTrue(spending > budget)


if __name__ == "__main__":
    unittest.main()
