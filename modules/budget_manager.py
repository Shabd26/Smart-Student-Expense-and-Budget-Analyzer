from modules.expense_manager import view_expenses
from utils.file_handler import load_data
from utils.file_handler import save_data

BUDGET_FILE = "data/budget.json"


def get_budget():
    default = {
        "monthly_budget": 0,
        "category_budgets": {}
    }

    return load_data(BUDGET_FILE, default)


def set_monthly_budget(amount):
    budget = get_budget()

    budget["monthly_budget"] = amount

    save_data(BUDGET_FILE, budget)

    return amount


def set_category_budget(category, amount):
    budget = get_budget()

    budget["category_budgets"][category] = amount

    save_data(BUDGET_FILE, budget)

    return amount


def get_month_expenses(expenses, month):
    result = []

    for expense in expenses:
        if expense["date"].startswith(month):
            result.append(expense)

    return result


def get_status(spent, budget):
    remaining = budget - spent

    if budget == 0:
        status = "not set"
        percentage = 0
    else:
        percentage = (spent / budget) * 100

        if spent > budget:
            status = "exceeded"
        elif percentage >= 80:
            status = "warning"
        else:
            status = "within limit"

    result = {
        "spent": spent,
        "budget": budget,
        "remaining": remaining,
        "utilization": percentage,
        "status": status
    }

    return result


def get_budget_status(month="2026-09"):
    budget = get_budget()

    expenses = view_expenses()
    expenses = get_month_expenses(expenses, month)

    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    categories = {}

    for category in budget["category_budgets"]:
        category_total = 0

        for expense in expenses:
            if expense["category"].lower() == category.lower():
                category_total = category_total + expense["amount"]

        category_budget = budget["category_budgets"][category]

        categories[category] = get_status(
            category_total,
            category_budget
        )

    result = {
        "month": month,
        "overall": get_status(
            total,
            budget["monthly_budget"]
        ),
        "categories": categories
    }

    return result


def check_budget_limits():
    report = get_budget_status()
    messages = []

    overall = report["overall"]

    if overall["status"] == "warning":
        messages.append("Overall budget is near the limit.")

    elif overall["status"] == "exceeded":
        messages.append("Overall budget has been exceeded.")

    for category in report["categories"]:
        status = report["categories"][category]["status"]

        if status == "warning":
            messages.append(
                category + " budget is near the limit."
            )

        elif status == "exceeded":
            messages.append(
                category + " budget has been exceeded."
            )

    return messages
