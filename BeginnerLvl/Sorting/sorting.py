import json
from datetime import date
movies = []


def sorted_by_rating():
    filter = movies[:]
    for i in range(len(filter)):
        for j in range(i+1, len(filter)):
            if filter[i]["Rating"] < filter[j]["Rating"]:
                filter[i], filter[j] = filter[j], filter[i]
    if not filter:
        print("No Record Found!")
    else:
        for rating in filter:
            name = rating["Name"]
            rating_value = rating["Rating"]
            date = rating["Date"]
            print(
                f"Name : {name} , Rating : {rating_value} , Date : {date}")


def sort_by_date():
    global movies

    sorted_by_date = sorted(movies, key=lambda x: x["Date"], reverse=True)

    for movie in sorted_by_date:
        name = movie["Name"]
        rating = movie["Rating"]
        date = movie["Date"]

        print(f"Name : {name} , Rating : {rating} , Date : {date}")


def add_entry(name, rating, date):
    movies.append({"Name": name, "Date": date, "Rating": rating})
    save_record()


def view_all_entries():
    if not movies:
        print("No Records Found")
    else:
        for record in movies:
            name = record["Name"]
            date = record["Date"]
            rating = record["Rating"]

            print(f"\nName : {name} , Rating : {rating} , Date : {date}\n")


def delete_record():
    view_all_entries()
    choice = int(input("Enter Record ID :"))
    index = choice - 1
    movies.pop(index)
    print("Record Deleted!")

    save_record()


def save_record():
    filepath = "Sorting/record.json"
    with open(filepath, "w") as f:
        json.dump(movies, f, indent=2)


def load_record():
    global movies
    filepath = "Sorting/record.json"
    try:
        with open(filepath) as f:
            movies = json.load(f)
            print("Save File Loaded!")
    except:
        print("Save File Not Found!..\nLoading New File\n")
        movies = []


load_record()

print("=="*6, "Welcome To Review System ", "=="*6)

print("Checking for Previous Save File\n")


while True:
    while True:
        print("\n1.Add movies/books with name and rating (1-10)\n"
              "2.View all entries\n3.View sorted by rating (highest first)\n"
              "4.View sorted by date added (newest first)"
              "\n5.Delete an entry")

        choice = int(input("Please Enter Choice:"))

        match choice:
            case 1:
                name = input("Enter name of movie/book:")
                rating = int(input("Enter your Rating from 1-10"))
                date = input("Enter Date for entering") or str(date.today())
                add_entry(name, rating, date)
                print("Record Added Sucessfully")
            case 2:
                view_all_entries()
            case 3:
                sorted_by_rating()
            case 4:
                sort_by_date()
            case 5:
                delete_record()
        break

    ch = input("Do you wish to continue(Yes/No)")
    if ch != "yes":
        print("GoodBye!")
        break
