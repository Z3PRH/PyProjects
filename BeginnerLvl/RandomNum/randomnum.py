import random

print("Welcome to Number Guessing...\n")
print("=="*6, "Rules", "=="*6,
      "\n1.User Gets Unlimited Attempts..\nWell that's it for Rules \n\n")

while True:

    secret_num = random.randint(1, 100)
    attempt = 0
    while True:
        usernum = int(input("Enter Number : "))
        if (usernum == secret_num):
            print("The user has Guessed the exact Number!!...Well done")
            print(
                f"UserNumber:{usernum}\nSysNumber:{secret_num}\nTotal Number of Attempts taken:{attempt}")
            break

        variable = f"Hint:Your Number is Less than Secret Number " if usernum < secret_num else "Hint:Your Number is Larger than Secret Number"
        attempt += 1
        print(variable)

    choice = input("Wanna Play Again?(Yes/No)").lower()
    if choice != "yes":
        print("Bye Bye!")
        break
