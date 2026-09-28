from utils.file_handler import load_data
from utils.file_handler import save_data

GOALS_FILE = "data/goals.json"


def get_goals():
    return load_data(GOALS_FILE, [])


def add_goal(name, target, saved):
    goals = get_goals()

    if len(goals) == 0:
        new_id = 1
    else:
        new_id = goals[-1]["id"] + 1

    goal = {
        "id": new_id,
        "name": name,
        "target": target,
        "saved": saved
    }

    goals.append(goal)

    save_data(GOALS_FILE, goals)

    return goal


def view_goals():
    return get_goals()


def add_savings(goal_id, amount):
    goals = get_goals()

    for goal in goals:
        if goal["id"] == goal_id:
            goal["saved"] = goal["saved"] + amount

            if goal["saved"] > goal["target"]:
                goal["saved"] = goal["target"]

            save_data(GOALS_FILE, goals)
            return True

    return False


def delete_goal(goal_id):
    goals = get_goals()

    for i in range(len(goals)):
        if goals[i]["id"] == goal_id:
            goals.pop(i)
            save_data(GOALS_FILE, goals)
            return True

    return False
