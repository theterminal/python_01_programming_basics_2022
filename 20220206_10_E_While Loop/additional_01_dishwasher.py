# 20220205 - Python - While Loop
# Additional 01 - Dishwasher - judge: https://judge.softuni.org/Contests/Practice/Index/1684#0


# user's input
num_bottles_dish_liquid_used = int(input())
num_dishes_to_wash = input()


# additional elements
cycle = num_pots = num_dishes = detergent = 0


# calculations
total_detergent_ml = num_bottles_dish_liquid_used * 750


# result
while num_dishes_to_wash != "End":
    num_dishes_to_wash = int(num_dishes_to_wash)
    cycle += 1

    if cycle % 3 == 0:
        num_pots += num_dishes_to_wash
        detergent_pots = num_dishes_to_wash * 15
        detergent += detergent_pots
    else:
        num_dishes += num_dishes_to_wash
        detergent_dishes = num_dishes_to_wash * 5
        detergent += detergent_dishes

    if detergent > total_detergent_ml:
        diff = abs(detergent - total_detergent_ml)
        print(f"Not enough detergent, {diff} ml. more necessary!")
        quit()

    num_dishes_to_wash = input()

    if num_dishes_to_wash == "End":
        break

print(f"Detergent was enough!")
print(f"{num_dishes} dishes and {num_pots} pots were washed.")
print(f"Leftover detergent {total_detergent_ml - detergent} ml.")
