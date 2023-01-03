# 20220206 - Python - While Loop
# Additional 02 - Report System - judge: https://judge.softuni.org/Contests/Practice/Index/1684#1


# user's input
money_expected_to_be_raised = int(input())
price_entered = input()


# additional elements
counter = money_received_total = money_received_cash = money_received_cc = counter_cash = counter_cc = 0


# calculations & result
while price_entered != "End":
    price_entered = int(price_entered)
    counter += 1

    if counter % 2 != 0:                                # cash transactions
        if price_entered > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            money_received_cash += price_entered
            counter_cash += 1
    else:                                               # card transactions
        if price_entered < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            money_received_cc += price_entered
            counter_cc += 1

    money_received_total = money_received_cash + money_received_cc

    if money_received_total >= money_expected_to_be_raised:
        break

    price_entered = input()

if price_entered == "End":
    print("Failed to collect required money for charity.")
    quit()

average_cash = money_received_cash / counter_cash
average_cc = money_received_cc / counter_cc
print(f"Average CS: {average_cash:.2f}")
print(f"Average CC: {average_cc:.2f}")
