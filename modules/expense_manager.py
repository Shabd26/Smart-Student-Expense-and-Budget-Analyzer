from utils.file_handler import load_data
from utils.file_handler import save_data
from utils.validation import check_amount
from utils.validation import check_category

EXPENSES_FILE = "data/expenses.json"


def get_expenses():
    return load_data(EXPENSES_FILE, [])


def add_expense(amount, category, description, date):
    if check_amount(amount) == False:
        return None

    if check_category(category) == False:
        return None

    expenses = get_expenses()

    if len(expenses) == 0:
        new_id = 1
    else:
        new_id = expenses[-1]["id"] + 1

    expense = {
        "id": new_id,
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    expenses.append(expense)
    save_data(EXPENSES_FILE, expenses)

    return expense


def view_expenses():
    return get_expenses()


def search_expenses(word):
    expenses = get_expenses()
    result = []

    word = word.lower()

    for expense in expenses:
        description = expense["description"].lower()
        category = expense["category"].lower()

        if word in description or word in category:
            result.append(expense)

    return result


def filter_expenses(category):
    expenses = get_expenses()
    result = []

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            result.append(expense)

    return result


def edit_expense(expense_id, amount, category, description, date):
    if check_amount(amount) == False:
        return False

    if check_category(category) == False:
        return False

    expenses = get_expenses()

    for expense in expenses:
        if expense["id"] == expense_id:
            expense["amount"] = amount
            expense["category"] = category
            expense["description"] = description
            expense["date"] = date

            save_data(EXPENSES_FILE, expenses)
            return True

    return False


def delete_expense(expense_id):
    expenses = get_expenses()

    for i in range(len(expenses)):
        if expenses[i]["id"] == expense_id:
            expenses.pop(i)
            save_data(EXPENSES_FILE, expenses)
            return True

    return False