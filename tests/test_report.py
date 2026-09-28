import unittest

from modules.analytics import calculate_total


class ReportTests(unittest.TestCase):

    def test_report_total(self):
        expenses = [
            {"amount": 500},
            {"amount": 1000}
        ]

        total = calculate_total(expenses)

        self.assertEqual(total, 1500)


if __name__ == "__main__":
    unittest.main()
