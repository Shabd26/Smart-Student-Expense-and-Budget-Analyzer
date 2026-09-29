# Smart Student Expense & Budget Analyzer

## 1. Problem Statement

Students often spend money on food, transport, study materials and entertainment without maintaining a proper record. This makes it difficult to understand spending patterns and manage a monthly budget.

The **Smart Student Expense & Budget Analyzer** is a command-line Python application that helps students record expenses, manage budgets, track income, manage savings goals and view basic financial analysis.

---

## 2. Scope

The project is designed for college students who want a simple way to manage their personal expenses.

The application provides:

- Expense management
- Budget management
- Spending analytics
- Financial goal management
- Income management
- Final report generation

The project is a local command-line application and stores data using JSON files.

---

## 3. Target Users

The main target users are:

- College students
- Students who want to track daily expenses
- Students who want to manage a monthly budget

---

## 4. Objectives

1. Record and manage student expenses.
2. Search and filter expense records.
3. Edit and delete existing expenses.
4. Set monthly and category-wise budgets.
5. Calculate basic spending statistics.
6. Analyze spending by category.
7. Track income and financial goals.
8. Generate a final financial report.
9. Apply fundamental Python programming concepts and algorithms.

---

## 5. Functional Requirements

### 5.1 Expense Management

- Add a new expense.
- View all expenses.
- Search expenses.
- Filter expenses by category.
- Edit an expense.
- Delete an expense.

### 5.2 Budget Management

- Set a monthly budget.
- Set category-wise budgets.
- View budget status.
- Check whether spending is within the budget.

### 5.3 Analytics

- Calculate total spending.
- Calculate average spending.
- Find the highest expense.
- Find the lowest expense.
- Calculate category-wise spending.
- Find the category with the highest spending.

### 5.4 Financial Goals

- Add a financial goal.
- View financial goals.
- Add savings to a goal.
- Delete a goal.

### 5.5 Income Management

- Store income.
- View stored income.

### 5.6 Report Generation

- Generate a summary containing income, expenses, analytics, budget information and financial goals.

---

## 6. Non-Functional Requirements

- **Usability:** The application should be simple to use through a command-line menu.
- **Reliability:** Important data should be saved in JSON files.
- **Performance:** Normal student records should be processed quickly.
- **Maintainability:** The application should be divided into separate Python modules.
- **Input Validation:** Basic validation should be used for important inputs.
- **Portability:** The application should run on a system with Python 3 installed.

---

## 7. Technology Used

- **Programming Language:** Python
- **Interface:** Command-Line Interface (CLI)
- **Data Storage:** JSON files
- **Testing:** Python unittest
- **Version Control:** Git and GitHub

---

## 8. Data Storage

The application uses four JSON files:

- `expenses.json` – stores expense records.
- `budget.json` – stores monthly and category budgets.
- `income.json` – stores income information.
- `goals.json` – stores financial goal information.

---

## 9. Project Modules

- `main.py` – Main menu and program flow.
- `expense_manager.py` – Expense operations.
- `budget_manager.py` – Budget operations.
- `analytics.py` – Spending calculations.
- `goal_manager.py` – Financial goal operations.
- `income_manager.py` – Income operations.
- `report_generator.py` – Final report generation.
- `file_handler.py` – JSON file handling.
- `validation.py` – Basic input validation.

---

## 10. Course Relevance

The project applies concepts from **CSE1021 – Introduction to Problem Solving and Programming**, including:

- Variables and data types
- Input and output
- Conditional statements
- Loops
- Functions
- Lists
- Dictionaries
- Searching
- Counting
- Summation
- Finding maximum and minimum values
- Basic file handling
- Modular programming
- Fundamental algorithms

---

## 11. Expected Outcome

The final application should allow a student to maintain basic financial records and understand their spending through simple calculations, budget checks and reports.

The project also demonstrates how fundamental Python programming concepts can be combined to solve a practical real-world problem.