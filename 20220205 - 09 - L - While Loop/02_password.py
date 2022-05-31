# 20220130 - Python Code
# Password

# user input
user_name = input()
password = input()
pass_to_check = input()

# calculations & results
while pass_to_check != password:
    pass_to_check = input()

print(f"Welcome {user_name}!")
