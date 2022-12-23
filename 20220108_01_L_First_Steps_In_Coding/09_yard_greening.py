# 20220108  - Python - Programming Basics
# 09 - Yard Greening - judge: https://judge.softuni.org/Contests/Compete/Index/2423#8
# pastebin: https://pastebin.com/077NJiC7


# user input
yard_size_sq_m = float(input())
cost_per_sq_m_lv = 7.61
percent_discount = 18


# calculations
cost_before_discount_lv = yard_size_sq_m * cost_per_sq_m_lv
decimal_discount_lv = cost_before_discount_lv * (percent_discount / 100)
total_cost_lv = cost_before_discount_lv - decimal_discount_lv


# output
print(f"The final price is: {total_cost_lv} lv.")
print(f"The discount is: {decimal_discount_lv} lv.")
