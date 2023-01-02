# 20220130 - Python - While Loop
# Note 01 - Create User ID / Password Log in


# user input
user_id = input("Enter User ID: ")
password = input("Enter password: ")


# calculations & results
i = 1

while password != "234H-23l":
    i += 1
    if i == 4:
        print("That's enough! Go have a drink! Your account is locked!")
        quit()
    password = input("Wrong password! Try again: ")

if i == 1:
    print(f"Welcome {user_id}!")
else:
    print(f"You got it this time {user_id}!")
