# Expense Tracker Code
# Features :
# 1.Add Expense
# 2.View Expenses
# 3.Delete Expense
# 4.View By Category
# 4.Save/Load Function (Ye i like this stuff :D)
# Optional : Adding a menu loop so User doesn't need to keep starting the code


import json  # required to create a file which store contents
from datetime import date  # Package which contains date , time , datetime etc

expense = []


def load_file():
    global expense
    try:
        with open("expense.json", "r")as f:
            expense = json.load(f)
            print("File Found ..\n Loading Contents ...")
    except:
        print("No Save File Found!")
        expense = []


def save_file():
    with open("expense.json", "w")as f:
        json.dump(expense, f, indent=2)


def add_expense(amount, category, date, description):
    expense.append({"Amount": amount, "Category": category,
                   "Date": date, "Description": description})
    save_file()


def view_expense():
    if not expense:
        print("None Entry found")
    else:
        for exp in expense:
            amt = exp["Amount"]
            category = exp["Category"]
            date = exp["Date"]
            descr = exp["Description"]
            print(
                f"Amount : {amt},Category : {category},Date : {date},Description : {descr} ")


def delete_expense():
    choice = int(
        input("Which Record should be deleted?...Enter Index Number "))
    index = choice - 1
    expense.pop(index)
    print("Record Permanently Delete!")
    save_file()


def view_by_category():
    category = input("Enter Category (Food/Transport/Other...) : ".lower())
    filter = [exp for exp in expense if exp["Category"].lower() == category]
# The first set of exp : it load the singular row set of item from the dictionary
# then the for loop runs through each item to check which item has that particular category
# so 1st exp : Store Individual row set of date

    if not filter:
        print("No Record for Particular Record found")
    else:
        for exp in filter:
            amt = exp["Amount"]
            category = exp["Category"]
            date = exp["Date"]
            descr = exp["Description"]
            print(
                f"Amount : {amt},Category : {category},Date : {date},Description : {descr} ")

    # Self Explanatory : just summing the amount
    total = sum(exp["Amount"] for exp in filter)
    print(f"Total Amount spent on {category} : {total}")


def total_amt():
    total = sum(exp["Amount"]for exp in expense)
    print(f"Total Amount : {total}")


load_file()

print("="*6, "Welcome to Expense Tracker Software", "="*6)
print("Choose From Below ")
while True:
    task = int(
        input("\n1.Add New Expense\n2.View All Expense\n3.Delete Expense\n4.View By Category\n5.Total Amount\n6.Exit\n"))
    match(task):
        case 1:
            amount = int(input("Enter Amount : "))
            category = input("Enter Category(Food/Transport/Other..) : ")
            date = input(
                "Enter set date or press enter to mark this day : ") or str(date.today())
            description = input("Enter Description : ") or "No Description"

            add_expense(amount, category, date, description)
        case 2:
            view_expense()
        case 3:
            delete_expense()
        case 4:
            view_by_category()
        case 5:
            total_amt()
        case 6:
            print("Thanks for Using ExTracker!")
            break
