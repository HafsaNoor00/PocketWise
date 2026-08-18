💰 PocketWise — Expense Tracker

A Python-based command-line expense tracker for managing and analyzing personal expenses.

PocketWise allows users to add, view, update, delete, and filter expenses while providing category-wise, monthly, and overall spending summaries. Expense data is stored persistently in a JSON file so it remains available after the program is closed.

✨ Features
➕ Add expenses with amount, category, date, description, and payment method
👀 View all saved expenses
✏️ Update existing expenses
🗑️ Delete expenses
🔎 Filter expenses by:
Category
Minimum amount
Date
Payment method
📊 Category-wise spending totals
💰 Total spending calculation
📈 Average expense calculation
⬆️ Highest expense tracking
⬇️ Lowest expense tracking
📅 Monthly spending statistics
💾 Persistent data storage using JSON
🛡️ Input validation and error handling
🆔 Automatically generated unique expense IDs
🚫 Duplicate expense detection
🛠️ Tech Stack
Python
JSON — persistent data storage
OOP — classes and objects
datetime — date validation
random — expense ID generation
📂 Project Structure
PocketWise/
│
├── Expense_tracker_pro.py
├── expenses.json
└── README.md
Main Components

Expense class

Represents an individual expense and stores its:

ID
Amount
Category
Date
Description
Payment method

ExpenseTracker class

Manages the expense collection and provides functionality for:

Adding expenses
Viewing expenses
Updating expenses
Deleting expenses
Filtering expenses
Category-wise totals
Expense summaries
Monthly statistics
Saving and loading data
🚀 Getting Started
Prerequisites

Make sure Python is installed on your system.

Check your Python version:

python --version
Installation

Clone the repository:

git clone <your-github-repository-url>

Navigate into the project directory:

cd PocketWise
Run the Application
python Expense_tracker_pro.py
💾 Data Persistence

PocketWise stores expense data in:

expenses.json

The application automatically loads previously saved expenses when it starts and saves changes when expenses are added, updated, or deleted.

📊 Expense Analysis

The application provides several ways to analyze spending:

Overall Summary

Displays:

Total spending
Number of expenses
Average expense
Highest expense
Lowest expense
Category-wise Totals

Groups expenses by category and calculates the total amount spent in each category.

Monthly Statistics

Allows users to enter a month in YYYY-MM format and view:

Total spending for that month
Number of expenses during that month
🛡️ Validation & Error Handling

The application validates:

Expense amount
Expense category
Date format
Description
Payment method
Expense ID

It also handles missing JSON data files without crashing the application.

🎯 Learning Objectives

This project was built to practice and demonstrate:

Object-Oriented Programming
Classes and objects
Dictionaries
Loops
Conditional statements
Functions
Lambda functions
sum(), max(), and min()
File handling
JSON serialization and deserialization
Input validation
Exception handling
Data filtering and aggregation
🔮 Future Improvements

Possible future enhancements include:

Search functionality
CSV export
Budget tracking
Data visualization
More advanced reporting
Automated testing
👩‍💻 Author

Hafsa Noor

Built as part of a Python/AI Engineering learning project.
