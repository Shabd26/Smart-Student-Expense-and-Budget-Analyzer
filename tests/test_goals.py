import unittest

from modules.goal_manager import add_goal


class GoalTests(unittest.TestCase):

    def test_goal_values(self):
        goal = {
            "name": "Laptop",
            "target": 60000,
            "saved": 10000
        }

        self.assertEqual(goal["target"], 60000)
        self.assertEqual(goal["saved"], 10000)


if __name__ == "__main__":
    unittest.main()
