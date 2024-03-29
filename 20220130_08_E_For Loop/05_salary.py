# 20220129 - Python - For Loop
# 05 - Salary - judge: https://judge.softuni.org/Contests/Compete/Index/2418#4


# ---------- version 1 ----------------


num_tabs_open = int(input())
salary = int(input())

for i in range(num_tabs_open):
    tab_entered = input()
    if tab_entered == "Facebook":
        salary -= 150
    elif tab_entered == "Instagram":
        salary -= 100
    elif tab_entered == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        quit()

print(round(salary))


# ---------- version 2 ----------------


# Python Code - Salary

num_tabs_open = int(input())
salary = int(input())

for i in range(num_tabs_open):
    tab = input()
    if tab == "Facebook":
        salary -= 150
    elif tab == "Instagram":
        salary -= 100
    elif tab == "Reddit":
        salary -= 50

if salary <= 0:
    print("You have lost your salary.")
else:
    print(round(salary))
