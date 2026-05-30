# Todo Manager

A simple command-line todo list application built with Python.

## What it does

Keep track of your tasks, mark them complete, and delete them when done. All todos are saved to a file, so they persist even after you close the program.

## Features

- ✅ Add new todos
- 👀 View all todos (with completion status)
- ✔️ Mark todos as complete
- ❌ Delete todos
- 💾 Save todos to file (auto-saves)
- 📂 Load todos from file (auto-loads on startup)

## How to use

1. Run the program:
```bash
python todo.py
```

2. Choose an option:
   - `1` - Add a new todo
   - `2` - View all todos
   - `3` - Mark a todo as done
   - `4` - Delete a todo
   - `5` - Exit

3. Your todos are automatically saved in `todos.json`

## Requirements

- Python 3.x
- No external libraries needed

## Files

- `todo.py` - Main program
- `todos.json` - Auto-created file where todos are saved