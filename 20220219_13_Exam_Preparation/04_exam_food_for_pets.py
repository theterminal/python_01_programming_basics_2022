# 20220219 - Python - Programming Basics - Exam Preparation
# 04 - Food For Pets - https://judge.softuni.org/Contests/Practice/Index/2275#6


# user input
num_days = int(input())
total_food = float(input())


# calculations & results
total_food_today, biscuits_current_day, total_biscuits = 0, 0, 0
counter_dog_food = counter_cat_food = 0

for current_day in range(1, num_days + 1):
    dog_food = int(input())
    cat_food = int(input())
    counter_dog_food += dog_food
    counter_cat_food += cat_food
    total_food_today = dog_food + cat_food

    if current_day % 3 == 0:
        biscuits_current_day = total_food_today * 0.1
        total_biscuits += biscuits_current_day

total_eaten = counter_dog_food + counter_cat_food
percent_food_eaten = total_eaten / total_food * 100
percent_dog_food = counter_dog_food / total_eaten * 100
percent_cat_food = counter_cat_food / total_eaten * 100

print(f"Total eaten biscuits: {round(total_biscuits)}gr.")
print(f"{percent_food_eaten:.2f}% of the food has been eaten.")
print(f"{percent_dog_food:.2f}% eaten from the dog.")
print(f"{percent_cat_food:.2f}% eaten from the cat.")
