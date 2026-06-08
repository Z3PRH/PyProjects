# Contact Manager
# Features :
# Add contact function
# View all contacts function
# Search by name function
# Delete contact function
import json
contact = []


def load_record():
    global contact
    try:
        with open("record.json")as f:
            contact = json.load(f)
            print("Record found ! .. Loading Contents")
    except:
        print("No Record found .... \n Loading Fresh Sheet")
        contact = []


def save_record():
    with open("record.json", "w")as f:
        json.dump(contact, f, indent=2)


def add_contact(name, number, email, address):
    contact.append({"Name": name, "PhoneNumber": number,
                    "Email": email, "Address": address})
    print("record Added!")
    save_record()


def view_contact():
    if not contact:
        print("no record found")
    else:
        for details in contact:
            name = details["Name"]
            pnum = details["PhoneNumber"]
            email = details["Email"]
            address = details["Address"]

            print(
                f"\nName:{name},\nPhoneNumber:{pnum},\nEmail:{email},\nAddress:{address}\n")


def search_by_name():
    name = input("Please Enter Name for the User you trying to find ")
    filter = [details for details in contact if details["Name"].lower()
              == name]
    if not filter:
        print("Entry for such a name not found")
    else:
        for record in filter:
            username = record["Name"]
            pnum = record["PhoneNumber"]
            email = record["Email"]
            address = record["Address"]

            print(
                f"\nName:{username},\nPhoneNumber:{pnum},\nEmail:{email},\nAddress:{address}\n")


def delete_contact():
    choice = int(input("Please enter the record id "))
    index = choice - 1
    contact.pop(index)
    print("Entry Deleted!")

    save_record()


def update_contact():
    view_contact()
    choice = int(input("Enter id of the record you want to edit :"))
    print("\n1.Name\n2.Phone Number \n3.Email \n4.Address")
    field = int(input("Enter which field you want to edit : "))
    index = choice - 1

    match field:
        case 1:
            contact[index]["Name"] = input("Set New Name As :")
        case 2:
            contact[index]["PhoneNumber"] = input("Enter New Contact Number :")
        case 3:
            contact[index]["Email"] = input("Enter New Email id :")
        case 4:
            contact[index]["Address"] = input("Enter Address:")
    print("contact Update!")
    save_record()

load_record()

print("=="*6, "Welcome To ContactMg!!", "=="*6)

while True:

    print("1.Add A New Record \n2.View All Record \n3.Search By Name \n4.Delete Record \n5.EditContact \n6.Exit")
    ch = int(input("Please Enter your Choice :"))
    match(ch):
        case 1:
            print("Please Enter Details Below \n")
            name = input("Name :")
            number = int(input("Phone Number :"))
            email = input("Email :")
            address = input("Address : ") or "Address not provided!"

            add_contact(name, number, email, address)

        case 2:
            view_contact()
        case 3:
            search_by_name()
        case 4:
            delete_contact()
        case 5:
            update_contact()
        case 6:
            print("Thanks for using ContactMg!")
            break
