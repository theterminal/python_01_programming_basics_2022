# 20220130 - Python Code
# Depositing money

# user input
balance = 0
deposit = input()

# calculations & results
if deposit == "NoMoreMoney":
    print(f"Total Deposited: {balance:.2f}")
    quit()
elif not deposit.isnumeric():
    print("Invalid entry: String!")
    quit()
elif float(deposit) < 0:
    print("Invalid Operation!")
    quit()

while deposit != "NoMoreMoney":
    balance += float(deposit)
    print(f"Increase: {float(deposit):.2f}")
    print(f"Sub Total: {balance:.2f}")
    deposit = input()

    if deposit == "NoMoreMoney":
        print(f"Total: {balance:.2f}")
        break
    elif not deposit.isnumeric():
        print("Invalid entry: String!")
        print(f"Total: {balance:.2f}")
        break
    elif float(deposit) < 0:
        print("Invalid Operation!")
        print(f"Total: {balance:.2f}")
        break
