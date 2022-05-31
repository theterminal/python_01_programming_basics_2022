# 20220130 - Python Code
# Game of Intervals

# user's input
number_turns = int(input())

# additional elements
points = 0
num_in_0_9 = num_in_10_19 = num_in_20_29 = num_in_30_39 = num_in_40_50 = num_invalid = 0

# calculations
for i in range(number_turns):
    number = int(input())

    if 0 <= number <= 9:
        points = points + number * 0.2
        num_in_0_9 += 1

    elif 10 <= number <= 19:
        points = points + number * 0.3
        num_in_10_19 += 1

    elif 20 <= number <= 29:
        points = points + number * 0.4
        num_in_20_29 += 1

    elif 30 <= number <= 39:
        points += 50
        num_in_30_39 += 1

    elif 40 <= number <= 50:
        points += 100
        num_in_40_50 += 1

    else:
        points /= 2
        num_invalid += 1

percent_0_9 = num_in_0_9 / number_turns * 100
percent_10_19 = num_in_10_19 / number_turns * 100
percent_20_29 = num_in_20_29 / number_turns * 100
percent_30_39 = num_in_30_39 / number_turns * 100
percent_40_50 = num_in_40_50 / number_turns * 100
percent_invalid = num_invalid / number_turns * 100

# result
print(f"{points:.2f}")
print(f"From 0 to 9: {percent_0_9:.2f}%")
print(f"From 10 to 19: {percent_10_19:.2f}%")
print(f"From 20 to 29: {percent_20_29:.2f}%")
print(f"From 30 to 39: {percent_30_39:.2f}%")
print(f"From 40 to 50: {percent_40_50:.2f}%")
print(f"Invalid numbers: {percent_invalid:.2f}%")
