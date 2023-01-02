# 20220130 - Python - For Loop
# Additional 01 - Back To The Past - judge: https://judge.softuni.org/Contests/Practice/Index/1680#0


# user's input
money_inherited = float(input())
year_to_live_to = int(input())

money_needed_odd, money_needed_even = 0, 0

for i in range(year_to_live_to - 1799):
    if i % 2 != 0:
        money_needed_odd += 12000 + 50 * (18 + i)
    else:
        money_needed_even += 12000

money_needed = money_needed_odd + money_needed_even
diff = abs(money_needed - money_inherited)


# result
if money_inherited >= money_needed:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")
