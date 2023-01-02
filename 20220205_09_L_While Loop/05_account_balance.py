# 20220130 - Python - While Loop
# 05 - Account Balance - judge: https://judge.softuni.org/Contests/Compete/Index/2419#4


# user input
deposit = input()


# calculations & results
balance = 0

while deposit != "NoMoreMoney":
    deposit = float(deposit)

    if deposit < 0:
        print("Invalid operation!")
        print(f"Total: {balance:.2f}")
        quit()

    balance += deposit
    print(f"Increase: {deposit:.2f}")
    deposit = input()

if deposit == "NoMoreMoney":
    print(f"Total: {balance:.2f}")
