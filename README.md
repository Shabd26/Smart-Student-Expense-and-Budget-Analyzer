# Smart Student Expense & Budget Analyzer

## Introduction

This is a simple Python command-line project for students. It helps a student keep track of expenses, income, budgets and savings goals.

The project is written using basic Python concepts such as:
- Variables
- Input and output
- if-else
- for and while loops
- Functions
- Lists
- Dictionaries
- Searching
- Counting
- Sum, maximum and minimum
- Basic file handling

JSON files are used only to save the program data.

## Main Features

1. Add an expense
2. View expenses
3. Search expenses
4. Filter expenses by category
5. Edit an expense
6. Delete an expense
7. Set a monthly budget
8. Set category budgets
9. Check budget status
10. View spending analytics
11. Add and track financial goals
12. Store income
13. Generate a final report

## How to Run

Open the project folder in a terminal and run:

```text
python main.py
```

## How to Test

Run:

```text
python -m unittest discover -s tests
```

## Project Structure

```text
Smart_Student_Expense_Budget_Analyzer/
│
├── main.py
├── README.md
├── statement.md
│
├── data/
│   ├── expenses.json
│   ├── budget.json
│   ├── income.json
│   └── goals.json
│
├── modules/
│   ├── expense_manager.py
│   ├── budget_manager.py
│   ├── analytics.py
│   ├── goal_manager.py
│   ├── income_manager.py
│   └── report_generator.py
│
├── utils/
│   ├── file_handler.py
│   └── validation.py
│
└── tests/
    ├── test_expenses.py
    ├── test_budget.py
    ├── test_analytics.py
    ├── test_goals.py
    ├── test_income.py
    └── test_report.py
```

## Course Relevance

The project mainly uses basic programming concepts taught in CSE1021:
- Problem solving
- Algorithms
- Variables and data types
- Input/output
- Selection statements
- Loops
- Functions
- Lists and dictionaries
- Basic algorithms such as summation, counting, searching, maximum and minimum
- Basic file handling

## Author

Shabd Mathur  
Registration Number: 26BAI10433  
VIT Bhopal University  
B.Tech CSE (Artificial Intelligence and Machine Learning)
