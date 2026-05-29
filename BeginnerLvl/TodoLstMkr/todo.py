# Todo List Maker
# Features:
# 1.Add A Task
# 2.View All Task
# 3.Marks Task as Completed
# 4.Delete/Remove a Task
# 5.Save/Load todos
# 6.Exit


import json

todos = []  # [] stand for an array which has empty data in them not NULL both Empty
completed = []  # same as todos[]


def load_todos():
    global todos
    try:
        # The R here stand for reading - user and only read them and cannot alter the contents
        with open("todos.json", "r")as f:
            todos = json.load(f)
        print("Todos Loaded")
    except:
        print("No Saved Todos Found")
        todos = []


def save_todos():
    # Similar to r W stands for writting / add or alter contents in the file
    with open("todos.json", "w") as f:
        # dump function is used to push those contents into the said file
        json.dump(todos, f, indent=2)


def add_task(task):
    todos.append({"Task": task, "Done": False})
    print("Task Added!")

    save_todos()


def view_task():
    if not todos:
        print("no task added")
    else:
        for i, todo in enumerate(todos):
            number = i+1
            task_name = todo["Task"]
            done_status = todo["Done"]
            print(f"Task {number} - {task_name}")
            print(f"Task Status - {done_status}")


def mark_task_completed():
    view_task()
    ch = int(input("Which Task? Enter number:"))
    index = ch - 1
    todos[index]["Done"] = True
    print(f"Task {ch} marked as done")

    save_todos()


def delete_task():
    view_task()
    ch = int(input("Which Task? Enter number:"))
    index = ch - 1
    todos.pop(index)
    print(f"Task {ch} has been deleted!")

    save_todos()


load_todos()

print("Welcome to Todo List Maker!")
while True:

    choice = int(
        input("\n1.Add Task\n2.View Task\n3.Mark Task as done\n4.Delete Task\n5.Exit\n"))
    if choice == 1:
        task = input("Enter Your Task : ")
        add_task(task)
    elif choice == 2:
        view_task()
    elif choice == 3:
        mark_task_completed()
    elif choice == 4:
        delete_task()
    else:
        print("Thanks for using Todo List Maker")
        break
