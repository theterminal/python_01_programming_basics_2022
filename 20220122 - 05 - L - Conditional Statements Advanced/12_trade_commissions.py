# Python Code - Trade Commissions

# user input
town = input().lower()
sales = float(input())

# calculations & results
town_names = ["sofia", "varna", "plovdiv"]
percent = 0

if town not in town_names or sales < 0:
    print("error")
    quit()

if town == "sofia":
    if 0 <= sales <= 500:
        percent = 0.05
    elif 500 < sales <= 1000:
        percent = 0.07
    elif 1000 < sales <= 10000:
        percent = 0.08
    elif sales > 10000:
        percent = 0.12
elif town == "varna":
    if 0 <= sales <= 500:
        percent = 0.045
    elif 500 < sales <= 1000:
        percent = 0.075
    elif 1000 < sales <= 10000:
        percent = 0.10
    elif sales > 10000:
        percent = 0.13
elif town == "plovdiv":
    if 0 <= sales <= 500:
        percent = 0.055
    elif 500 < sales <= 1000:
        percent = 0.08
    elif 1000 < sales <= 10000:
        percent = 0.12
    elif sales > 10000:
        percent = 0.145

result = sales * percent
print(f"{result:.2f}")
