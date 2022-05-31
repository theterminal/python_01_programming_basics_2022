# 20220130 - Python Code
# Account Balance

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
