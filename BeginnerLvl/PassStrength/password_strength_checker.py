# Password_checker is a CLI APP which grabs a input .. i.e, password from the user then ran them through a
# series of check and gives them a strength rating(Weak/Medium/Strong)

def check_strength(password):
    global score
    special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/~`)"
    special=any(char in special_chars for char in password)
    hasupper = any(char.isupper() for char in password)
    haslower = any(char.islower() for char in password)
    hasdigits = any(char.isdigit() for char in password)
    while True:
        if (special):
            score += 1
        if (len(password) >= 8):
            score += 1
        if (hasupper):
            score += 1
        if (haslower):
            score += 1
        if (hasdigits):
            score += 1
        break
    return score


score = 0
print("=="*6, "Welcome to Password Strength Checker", "=="*6)
while True:
    while True:
        password = input("Enter Password to Check : ")
        if not password:
            print("Please Enter your password...as Null Entries if not be accepted")
        else:
            print("Running  Tests..")
            result = check_strength(password)
            print(f"Password Total Score :{result}")
            break
    if (result == 5):
        print("The Passoword Contain UpperCase,LowerCase,Digits and has Character length more than 8")
    elif (score == 4):
        print("The Password is Great...But you can improve by combining password with upper,lower or special chars and length more than 8")
    elif (score == 3):
        print("Ooof!..Not the Ideal password ... change is recommeded")
    else:
        print("Bruh!..you Bounded to get your Account Stolen")

    choice = input("Do You Wish to Check Again(Yes/No)?")
    if choice !="yes":
        print("Adios Amigo")
        break
    else:
        score = 0
