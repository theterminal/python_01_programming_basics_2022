# 20220109 - Python - Programming Basics
# 03 - Deposit Calculator - judge: https://judge.softuni.org/Contests/Compete/Index/2424#2
# pastebin: https://pastebin.com/1DzyN460


# user input
amount_deposited = float(input())
term_in_months = int(input())
yearly_APR = float(input())


# calculations
real_APR_for_1_m = ((yearly_APR / 100) / 12)
interest = amount_deposited * real_APR_for_1_m * term_in_months
total_amount = amount_deposited + interest


# output
print(total_amount)
