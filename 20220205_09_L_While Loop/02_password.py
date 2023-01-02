# 20220130  - Python - While Loop
# 02 - Password - judge: https://judge.softuni.org/Contests/Compete/Index/2419#1


# user input
user_name = input()
password = input()
pass_to_check = input()


# calculations & results
while pass_to_check != password:
    pass_to_check = input()

print(f"Welcome {user_name}!")
