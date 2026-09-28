import unittest

from modules.analytics import calculate_total
from modules.analytics import calculate_average
from modules.analytics import find_highest_expense
from modules.analytics import find_lowest_expense
from modules.analytics import category_analysis
from modules.analytics import count_transactions


class AnalyticsTests(unittest.TestCase):

    def setUp(self):
        self.expenses = [
            {
                "id": 1,
                "amount": 100,
                "category": "Food"
            },
            {
                "id": 2,
                "amount": 300,
                "category": "Study"
            },
            {
                "id": 3,
                "amount": 200,
                "category": "Food"
            }
        ]

    def test_total(self):
        self.assertEqual(
            calculate_total(self.expenses),
            600
        )

    def test_average(self):
        self.assertEqual(
            calculate_average(self.expenses),
            200
        )

    def test_highest(self):
        result = find_highest_expense(self.expenses)
        self.assertEqual(result["amount"], 300)

    def test_lowest(self):
        result = find_lowest_expense(self.expenses)
        self.assertEqual(result["amount"], 100)

    def test_category(self):
        result = category_analysis(self.expenses)
        self.assertEqual(result["Food"], 300)

    def test_count(self):
        self.assertEqual(
            count_transactions(self.expenses),
            3
        )


if __name__ == "__main__":
    unittest.main()
