import unittest


class IncomeTests(unittest.TestCase):

    def test_income(self):
        income = 25000
        spending = 850

        remaining = income - spending

        self.assertEqual(remaining, 24150)


if __name__ == "__main__":
    unittest.main()
