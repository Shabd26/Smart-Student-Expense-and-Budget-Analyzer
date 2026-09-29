# Smart Student Expense & Budget Analyzer

## 1. Problem Statement

Students often have to manage their daily expenses, monthly budgets, income, and savings goals. When this information is maintained manually, it can be difficult to track spending and understand where money is being used.

The Smart Student Expense & Budget Analyzer is a Python-based command-line application that helps students record expenses, manage budgets, track income and financial goals, and analyze their spending.

---

## 2. Scope

The project focuses on basic personal financial management for students.

The system allows users to:

- Add, view, search, filter, edit, and delete expenses.
- Set monthly and category-wise budgets.
- View budget usage and warnings.
- Calculate total and average spending.
- Find the highest and lowest expenses.
- Analyze spending by category.
- Set and track financial goals.
- Record income.
- Generate a final financial report.

The project is designed for individual student use and does not include online banking, payment processing, or direct connection to bank accounts.

---

## 3. Target Users

The main target users are:

- College students.
- Students who want to track their daily expenses.
- Students who want to manage monthly budgets.
- Students who want to monitor savings goals.

---

## 4. Objectives

The main objectives of the project are:

1. To provide a simple way to record and manage student expenses.
2. To help students monitor monthly and category-wise budgets.
3. To calculate useful spending statistics.
4. To track income and financial goals.
5. To generate a summary of the user's financial information.
6. To apply Python programming concepts learned in CSE1021.

---

## 5. Functional Requirements

### FR1 - Expense Management

The system should allow the user to:

- Add a new expense.
- View all expenses.
- Search expenses using a word.
- Filter expenses by category.
- Edit an existing expense.
- Delete an expense.

### FR2 - Budget Management

The system should allow the user to:

- Set a monthly budget.
- Set budgets for individual categories.
- View budget status.
- Check whether a budget is near or above its limit.

### FR3 - Expense Analytics

The system should calculate:

- Total spending.
- Average expense.
- Highest expense.
- Lowest expense.
- Category-wise spending.
- Number of transactions.

### FR4 - Financial Goal Management

The system should allow the user to:

- Add a financial goal.
- View existing goals.
- Add savings to a goal.
- Delete a goal.
- Track the progress of a goal.

### FR5 - Income Management

The system should allow the user to:

- Set income.
- View the current income amount.

### FR6 - Financial Report

The system should generate a final report containing:

- Income.
- Total spending.
- Remaining money.
- Average expense.
- Highest and lowest expenses.
- Category-wise spending.
- Budget status.
- Financial goals.

---

## 6. Non-Functional Requirements

### NFR1 - Usability

The system should provide a simple command-line interface with clear menus and easy-to-understand instructions.

### NFR2 - Reliability

The system should correctly save and retrieve expense, budget, income, and goal data during normal use.

### NFR3 - Performance

The system should perform common operations such as adding, searching, editing, deleting, and analyzing expenses quickly for normal student-sized datasets.

### NFR4 - Maintainability

The system should use separate modules and functions so that individual features can be understood, tested, and modified easily.

### NFR5 - Input Validation

The system should validate important inputs, such as preventing zero or negative expense amounts and empty categories.

### NFR6 - Portability

The system should run on systems that have Python installed without requiring specialized hardware or software.

---

## 7. Technology Used

- **Programming Language:** Python
- **Interface:** Command-Line Interface (CLI)
- **Data Storage:** JSON files
- **Testing:** Python unittest
- **Version Control:** Git and GitHub

No external Python libraries are required.

---

## 8. Data Storage

The application uses JSON files to store data.

The main data files are:

- `expenses.json` - Stores expense records.
- `budget.json` - Stores monthly and category budgets.
- `goals.json` - Stores financial goals and savings.
- `income.json` - Stores income information.

This allows data to remain available when the program is closed and opened again.

---

## 9. Project Modules

The project is divided into separate modules:

### `expense_manager.py`

Handles adding, viewing, searching, filtering, editing, and deleting expenses.

### `budget_manager.py`

Handles monthly and category budgets, budget status, and budget warnings.

### `analytics.py`

Performs calculations such as total, average, highest, lowest, and category-wise spending.

### `goal_manager.py`

Handles financial goals, savings, goal viewing, and deletion.

### `income_manager.py`

Handles storing and retrieving income.

### `report_generator.py`

Combines financial information and generates the final report.

### `file_handler.py`

Handles reading and writing JSON data files.

### `validation.py`

Performs basic validation of important user inputs.

### `main.py`

Provides the command-line menus and connects the different modules.

---

## 10. Course Relevance

The project is directly related to the CSE1021 - Introduction to Problem Solving and Programming course.

The project applies the following Python concepts:

- Variables and data types.
- Input and output.
- Arithmetic operations.
- Conditional statements.
- `for` and `while` loops.
- Functions.
- Lists.
- Dictionaries.
- Searching.
- Counting.
- Summation.
- Finding maximum and minimum values.
- Basic data processing.
- File handling.
- Modular programming.

The project uses these concepts to solve a practical student expense-management problem.

---

## 11. Expected Outcome

The expected outcome is a simple Python application that helps students manage and understand their personal financial information.

The completed system should allow users to manage expenses, budgets, income, and financial goals through a command-line interface and generate useful spending information through analytics and reports.
