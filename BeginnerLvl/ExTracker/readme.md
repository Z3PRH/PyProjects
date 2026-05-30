# Expense Tracker

A simple command-line expense tracking application built with Python.

## What it does

Track your daily expenses by category, view spending patterns, and manage your budget. All expenses are automatically saved, so your data persists even after closing the program.

## Features

- ✅ Add new expenses (amount, category, date, description)
- 👀 View all expenses
- 💰 View total amount spent
- 🏷️ View expenses by category (filter)
- ❌ Delete expenses
- 💾 Auto-save/load expenses (data persists)
- 📅 Auto-date (uses today's date if not specified)

## How to use

1. Run the program:
```bash
python ExpenseTracker.py
```

2. Choose an option from the menu:
   - `1` - Add a new expense
   - `2` - View all expenses
   - `3` - Delete an expense
   - `4` - View expenses by category
   - `5` - View total amount spent
   - `6` - Exit

3. Your expenses are automatically saved in `expense.json`

## Requirements

- Python 3.x
- No external libraries needed (uses built-in `json` and 'datetime')

## Files

- `ExpenseTracker.py` - Main program
- `expense.json` - Auto-created file where expenses are saved

make sure the json file is within the expensefolder ..sometimes if outside it may not show the saved contents 

## Example

```
Add expense: Amount: 100, Category: food, Date: 2026-05-30
View by category: food -> Shows all food expenses + total spent on food
Total amount: 250 -> Shows total spent across all categories
```