def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    return total


def calculate_average(expenses):
    if len(expenses) == 0:
        return 0

    total = calculate_total(expenses)
    average = total / len(expenses)

    return average


def find_highest_expense(expenses):
    if len(expenses) == 0:
        return None

    highest = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    return highest


def find_lowest_expense(expenses):
    if len(expenses) == 0:
        return None

    lowest = expenses[0]

    for expense in expenses:
        if expense["amount"] < lowest["amount"]:
            lowest = expense

    return lowest


def category_analysis(expenses):
    totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in totals:
            totals[category] = 0

        totals[category] = totals[category] + amount

    return totals


def find_highest_category(totals):
    if len(totals) == 0:
        return None

    highest_category = None
    highest_amount = 0

    for category in totals:
        if totals[category] > highest_amount:
            highest_amount = totals[category]
            highest_category = category

    return highest_category


def count_transactions(expenses):
    return len(expenses)
