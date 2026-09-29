from modules.expense_manager import add_expense
from modules.expense_manager import view_expenses
from modules.expense_manager import search_expenses
from modules.expense_manager import filter_expenses
from modules.expense_manager import edit_expense
from modules.expense_manager import delete_expense

from modules.budget_manager import set_monthly_budget
from modules.budget_manager import set_category_budget
from modules.budget_manager import get_budget_status
from modules.budget_manager import check_budget_limits

from modules.analytics import calculate_total
from modules.analytics import calculate_average
from modules.analytics import find_highest_expense
from modules.analytics import find_lowest_expense
from modules.analytics import category_analysis

from modules.goal_manager import add_goal
from modules.goal_manager import view_goals
from modules.goal_manager import add_savings
from modules.goal_manager import delete_goal

from modules.income_manager import set_income
from modules.income_manager import get_income_amount

from modules.report_generator import generate_report
from modules.report_generator import display_report


def show_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses found.")
    else:
        print("\nID  Amount  Category  Description  Date")

        for expense in expenses:
            print(
                expense["id"],
                expense["amount"],
                expense["category"],
                expense["description"],
                expense["date"]
            )


def expense_menu():
    while True:
        print("\n--- Expense Menu ---")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Search expenses")
        print("4. Filter expenses")
        print("5. Edit expense")
        print("6. Delete expense")
        print("7. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            date = input("Enter date (YYYY-MM-DD): ")

            result = add_expense(amount, category, description, date)

            if result != None:
                print("Expense added.")

        elif choice == "2":
            expenses = view_expenses()
            show_expenses(expenses)

        elif choice == "3":
            word = input("Enter search word: ")
            expenses = search_expenses(word)
            show_expenses(expenses)

        elif choice == "4":
            category = input("Enter category: ")
            expenses = filter_expenses(category)
            show_expenses(expenses)

        elif choice == "5":
            expense_id = int(input("Enter expense ID: "))
            amount = float(input("Enter new amount: "))
            category = input("Enter new category: ")
            description = input("Enter new description: ")
            date = input("Enter new date: ")

            result = edit_expense(
                expense_id,
                amount,
                category,
                description,
                date
            )

            if result == True:
                print("Expense updated.")

        elif choice == "6":
            expense_id = int(input("Enter expense ID: "))

            result = delete_expense(expense_id)

            if result == True:
                print("Expense deleted.")
            else:
                print("Expense not found.")

        elif choice == "7":
            break

        else:
            print("Invalid choice.")


def budget_menu():
    while True:
        print("\n--- Budget Menu ---")
        print("1. Set monthly budget")
        print("2. Set category budget")
        print("3. View budget status")
        print("4. Check warnings")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = float(input("Enter monthly budget: "))
            set_monthly_budget(amount)
            print("Budget saved.")

        elif choice == "2":
            category = input("Enter category: ")
            amount = float(input("Enter category budget: "))
            set_category_budget(category, amount)
            print("Category budget saved.")

        elif choice == "3":
            report = get_budget_status()

            print("Month:", report["month"])
            print("Overall:", report["overall"])

            for category in report["categories"]:
                print(category, report["categories"][category])

        elif choice == "4":
            messages = check_budget_limits()

            if len(messages) == 0:
                print("No warnings.")
            else:
                for message in messages:
                    print(message)

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


def analytics_menu():
    expenses = view_expenses()

    total = calculate_total(expenses)
    average = calculate_average(expenses)

    print("\n--- Analytics ---")
    print("Total spending:", total)
    print("Average spending:", average)

    highest = find_highest_expense(expenses)
    lowest = find_lowest_expense(expenses)

    if highest != None:
        print("Highest expense:", highest)

    if lowest != None:
        print("Lowest expense:", lowest)

    print("Category totals:")

    totals = category_analysis(expenses)

    for category in totals:
        print(category, totals[category])


def goal_menu():
    while True:
        print("\n--- Goal Menu ---")
        print("1. Add goal")
        print("2. View goals")
        print("3. Add savings")
        print("4. Delete goal")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter goal name: ")
            target = float(input("Enter target amount: "))
            saved = float(input("Enter saved amount: "))

            add_goal(name, target, saved)
            print("Goal added.")

        elif choice == "2":
            goals = view_goals()

            if len(goals) == 0:
                print("No goals found.")
            else:
                for goal in goals:
                    print(goal)

        elif choice == "3":
            goal_id = int(input("Enter goal ID: "))
            amount = float(input("Enter savings amount: "))

            result = add_savings(goal_id, amount)

            if result == True:
                print("Savings added.")
            else:
                print("Goal not found.")

        elif choice == "4":
            goal_id = int(input("Enter goal ID: "))

            result = delete_goal(goal_id)

            if result == True:
                print("Goal deleted.")
            else:
                print("Goal not found.")

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


def income_menu():
    print("\n--- Income ---")

    amount = float(input("Enter income: "))
    set_income(amount)

    print("Income saved.")
    print("Current income:", get_income_amount())


def main():
    while True:
        print("\n==============================")
        print(" Smart Student Expense Analyzer")
        print("==============================")
        print("1. Expense Management")
        print("2. Budget Management")
        print("3. Analytics")
        print("4. Financial Goals")
        print("5. Income Management")
        print("6. Final Report")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            expense_menu()

        elif choice == "2":
            budget_menu()

        elif choice == "3":
            analytics_menu()

        elif choice == "4":
            goal_menu()

        elif choice == "5":
            income_menu()

        elif choice == "6":
            report = generate_report()
            display_report(report)

        elif choice == "7":
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


main()
