# 20220205 - Python Code
# Vacation

# user input
money_needed_for_vacation = float(input())
money_on_hand = float(input())

# calculations & results:
continues_days, total_days_passed = 0, 0

while money_on_hand < money_needed_for_vacation:
    action_entered = input()
    amount_entered = float(input())
    total_days_passed += 1

    if action_entered == "spend":
        continues_days += 1

        if continues_days == 5:
            print("You can't save the money.")
            print(f"{total_days_passed}")
            quit()

        money_on_hand -= amount_entered

        if money_on_hand < 0:
            money_on_hand = 0
    else:
        money_on_hand += amount_entered
        continues_days = 0

print(f"You saved the money for {total_days_passed} days.")

# ------- another version --------------------------------

# # Python Code - Vacation
#
# # user input
# money_needed_for_vacation = float(input())
# money_on_hand = float(input())
#
# # calculations & results
# action, counter_spend, counter_days, money = "", 0, 0, 0
#
# while True:
#     action = input()
#     money = float(input())
#     counter_days += 1
#
#     if action == "spend":
#         counter_spend += 1
#         if money > money_on_hand:
#             money_on_hand = 0
#         else:
#             money_on_hand -= money
#         if counter_spend == 5:
#             print("You can't save the money.")
#             print(f"{counter_days}")
#             break
#     else:
#         money_on_hand += money
#         counter_spend = 0
#         if money_on_hand >= money_needed_for_vacation:
#             print(f"You saved the money for {counter_days} days.")
#             break
