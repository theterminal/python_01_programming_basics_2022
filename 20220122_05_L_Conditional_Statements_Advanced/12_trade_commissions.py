# 20220120 - Python - Conditional Statements Advanced
# 12 - Trade Commissions - judge: https://judge.softuni.org/Contests/Compete/Index/2415#11


# user input
town_entered = input().lower()
sales_entered = float(input())


# calculations & results
town_names = ["sofia", "varna", "plovdiv"]
percent = 0

if town_entered not in town_names or sales_entered < 0:
    print("error")
    quit()

if town_entered == "sofia":
    if 0 <= sales_entered <= 500:
        percent = 0.05
    elif 500 < sales_entered <= 1000:
        percent = 0.07
    elif 1000 < sales_entered <= 10000:
        percent = 0.08
    elif sales_entered > 10000:
        percent = 0.12
elif town_entered == "varna":
    if 0 <= sales_entered <= 500:
        percent = 0.045
    elif 500 < sales_entered <= 1000:
        percent = 0.075
    elif 1000 < sales_entered <= 10000:
        percent = 0.10
    elif sales_entered > 10000:
        percent = 0.13
elif town_entered == "plovdiv":
    if 0 <= sales_entered <= 500:
        percent = 0.055
    elif 500 < sales_entered <= 1000:
        percent = 0.08
    elif 1000 < sales_entered <= 10000:
        percent = 0.12
    elif sales_entered > 10000:
        percent = 0.145

result = sales_entered * percent
print(f"{result:.2f}")
