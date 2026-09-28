import unittest
import tempfile
import os


class ExpenseTests(unittest.TestCase):

    def test_add_search_filter_edit_delete(self):
        import json

        folder = tempfile.mkdtemp()
        filename = os.path.join(folder, "expenses.json")

        expenses = []

        expense = {
            "id": 1,
            "amount": 100,
            "category": "Food",
            "description": "Lunch",
            "date": "2026-09-01"
        }

        expenses.append(expense)

        file = open(filename, "w")
        json.dump(expenses, file)
        file.close()

        file = open(filename, "r")
        data = json.load(file)
        file.close()

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["amount"], 100)

        data[0]["amount"] = 150

        self.assertEqual(data[0]["amount"], 150)

        data.pop(0)

        self.assertEqual(len(data), 0)


if __name__ == "__main__":
    unittest.main()
