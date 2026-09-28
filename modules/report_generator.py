from modules.expense_manager import view_expenses
from modules.income_manager import get_income_amount
from modules.analytics import calculate_total
from modules.analytics import calculate_average
from modules.analytics import find_highest_expense
from modules.analytics import find_lowest_expense
from modules.analytics import category_analysis
from modules.analytics import find_highest_category
from modules.analytics import count_transactions
from modules.budget_manager import get_budget_status
from modules.goal_manager import view_goals


def generate_report():
    expenses = view_expenses()

    income = get_income_amount()
    total = calculate_total(expenses)
    average = calculate_average(expenses)

    highest = find_highest_expense(expenses)
    lowest = find_lowest_expense(expenses)

    categories = category_analysis(expenses)
    highest_category = find_highest_category(categories)

    count = count_transactions(expenses)

    budget = get_budget_status()
    goals = view_goals()

    report = {
        "income": income,
        "total_spending": total,
        "remaining_money": income - total,
        "average_expense": average,
        "highest_expense": highest,
        "lowest_expense": lowest,
        "category_totals": categories,
        "highest_category": highest_category,
        "transaction_count": count,
        "budget_status": budget,
        "goals": goals
    }

    return report


def display_report(report):
    print("\n========== FINAL REPORT ==========")

    print("Income:", report["income"])
    print("Total spending:", report["total_spending"])
    print("Remaining money:", report["remaining_money"])
    print("Average expense:", report["average_expense"])
    print("Transactions:", report["transaction_count"])

    print("\nHighest expense:")
    print(report["highest_expense"])

    print("\nLowest expense:")
    print(report["lowest_expense"])

    print("\nCategory totals:")

    for category in report["category_totals"]:
        print(
            category,
            ":",
            report["category_totals"][category]
        )

    print(
        "Highest category:",
        report["highest_category"]
    )

    print("\nBudget:")
    print(report["budget_status"]["overall"])

    print("\nGoals:")

    for goal in report["goals"]:
        print(goal)

    print("==================================")
