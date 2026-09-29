import unittest
import tempfile
import os

from modules import goal_manager


class GoalTests(unittest.TestCase):

    def setUp(self):
        self.folder = tempfile.mkdtemp()
        self.file = os.path.join(self.folder, "goals.json")
        self.old_file = goal_manager.GOALS_FILE
        goal_manager.GOALS_FILE = self.file

    def tearDown(self):
        goal_manager.GOALS_FILE = self.old_file

    def test_add_goal(self):
        goal = goal_manager.add_goal("Laptop", 60000, 10000)
        self.assertEqual(goal["name"], "Laptop")
        self.assertEqual(goal["target"], 60000)
        self.assertEqual(goal["saved"], 10000)

    def test_add_savings(self):
        goal_manager.add_goal("Laptop", 60000, 10000)
        result = goal_manager.add_savings(1, 5000)
        self.assertTrue(result)
        self.assertEqual(goal_manager.view_goals()[0]["saved"], 15000)

    def test_delete_goal(self):
        goal_manager.add_goal("Laptop", 60000, 10000)
        result = goal_manager.delete_goal(1)
        self.assertTrue(result)
        self.assertEqual(len(goal_manager.view_goals()), 0)


if __name__ == "__main__":
    unittest.main()
