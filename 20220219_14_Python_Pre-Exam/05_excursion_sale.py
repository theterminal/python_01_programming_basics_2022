# 20220219 - Python - Programming Basics - Pre-Exam
# 05 - Excursion Sale - judge: https://judge.softuni.org/Contests/Compete/Index/3351#4


# user information
num_sea_vac = int(input())
num_mountain_vac = int(input())

vac_pack_entered = input()


# calculations & results
profit = 0

while vac_pack_entered != "Stop":
    if vac_pack_entered == "sea" and num_sea_vac > 0:
        profit += 680
        num_sea_vac -= 1
    elif vac_pack_entered == "see":
        profit += 0
    elif vac_pack_entered == "mountain" and num_mountain_vac > 0:
        profit += 499
        num_mountain_vac -= 1
    elif vac_pack_entered == "mountain":
        profit += 0

    if num_sea_vac == 0 and num_mountain_vac == 0:
        print(f"Good job! Everything is sold.")
        print(f"Profit: {profit} leva.")
        quit()

    vac_pack_entered = input()

print(f"Profit: {profit} leva.")
