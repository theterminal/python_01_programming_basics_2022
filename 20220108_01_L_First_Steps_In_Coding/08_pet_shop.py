# 20220108 - Python - Programming Basics
# 08 - Pet Shop - judge: https://judge.softuni.org/Contests/Compete/Index/2423#7
# pastebin: https://pastebin.com/c7MX5KQn


# user input
number_dog_food_packages = int(input())
number_cat_food_packages = int(input())
cost_dog_food_per_package_lv = 2.50
cost_cat_food_per_package_lv = 4


# calculations
cost_all_dog_food = number_dog_food_packages * cost_dog_food_per_package_lv
cost_all_cat_food = number_cat_food_packages * cost_cat_food_per_package_lv
total_cost_all_food = cost_all_dog_food + cost_all_cat_food


# output
print(f"{total_cost_all_food} lv.")
