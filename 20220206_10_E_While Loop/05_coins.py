# 20220205 - Python - While Loop
# 05 - Coins - judge: https://judge.softuni.org/Contests/Compete/Index/2420#4


# -------------------- version 1 ----------------------------


# user input
amount_entered = float(input())
change = amount_entered


# calculations & results
change = int(change * 100)
counter = 0

while change != 0:

    if change // 200 >= 1:
        change -= 200
        counter += 1
    elif change // 100 >= 1:
        change -= 100
        counter += 1
    elif change // 50 >= 1:
        change -= 50
        counter += 1
    elif change // 20 >= 1:
        change -= 20
        counter += 1
    elif change // 10 >= 1:
        change -= 10
        counter += 1
    elif change // 5 >= 1:
        change -= 5
        counter += 1
    elif change // 2 >= 1:
        change -= 2
        counter += 1
    elif change // 1 >= 1:
        change -= 1
        counter += 1

print(counter)


# -------------------- version 2 ----------------------------


# user's input
change = float(input())                 # It is not good idea to use float! Try using int instead. See the next\
                                        # solution of the problem delete_me.py

# additional elements
num_2_lv = 0
num_1_lv = 0
num_050_lv = 0
num_020_lv = 0
num_010_lv = 0
num_005_lv = 0
num_002_lv = 0
num_001_lv = 0

# result
while change != 0:
    change = round(change, 2)
    if change >= 2:
        while change >= 2:
            num_2_lv += 1
            change -= 2
    elif change >= 1:
        while change >= 1:
            num_1_lv += 1
            change -= 1
    elif change >= 0.50:
        while change >= 0.5:
            num_050_lv += 1
            change -= 0.5
    elif change >= 0.20:
        while change >= 0.2:
            num_020_lv += 1
            change -= 0.2
    elif change >= 0.10:
        while change >= 0.1:
            num_010_lv += 1
            change -= 0.1
    elif change >= 0.05:
        while change >= 0.05:
            num_005_lv += 1
            change -= 0.05
    elif change >= 0.02:
        while change >= 0.02:
            num_002_lv += 1
            change -= 0.02
    elif change >= 0.01:
        while change >= 0.01:
            num_001_lv += 1
            change -= 0.01

total = num_2_lv + num_1_lv + num_050_lv + num_020_lv + num_010_lv + num_005_lv + num_002_lv + num_001_lv
print(f"total number of coins {total}")

# KK added some text and results!
print(f"number 2 lv coins: {num_2_lv}")
print(f"number 1 lv coins: {num_1_lv}")
print(f"number 0.50 lv coins: {num_050_lv}")
print(f"number 0.20 lv coins: {num_020_lv}")
print(f"number 0.10 lv coins: {num_010_lv}")
print(f"number 0.05 lv coins: {num_005_lv}")
print(f"number 0.02 lv coins: {num_002_lv}")
print(f"number 0.01 lv coins: {num_001_lv}")


# -------------------- version 3 ----------------------------


# user's input
change = float(input())
change = int(change * 100)

# additional elements
num_2_lv = 0
num_1_lv = 0
num_050_lv = 0
num_020_lv = 0
num_010_lv = 0
num_005_lv = 0
num_002_lv = 0
num_001_lv = 0

# result
while change != 0:
    if change >= 200:
        while change >= 200:
            num_2_lv += 1
            change -= 200
    elif change >= 100:
        while change >= 100:
            num_1_lv += 1
            change -= 100
    elif change >= 50:
        while change >= 50:
            num_050_lv += 1
            change -= 50
    elif change >= 20:
        while change >= 20:
            num_020_lv += 1
            change -= 20
    elif change >= 10:
        while change >= 10:
            num_010_lv += 1
            change -= 10
    elif change >= 5:
        while change >= 5:
            num_005_lv += 1
            change -= 5
    elif change >= 2:
        while change >= 2:
            num_002_lv += 1
            change -= 2
    elif change >= 1:
        while change >= 1:
            num_001_lv += 1
            change -= 1

total = num_2_lv + num_1_lv + num_050_lv + num_020_lv + num_010_lv + num_005_lv + num_002_lv + num_001_lv
print(f"total coins {total}")

# KK added some text and results!
print(f"coin 2 lv: {num_2_lv}")
print(f"coin 1 lv: {num_1_lv}")
print(f"coin 50 st: {num_050_lv}")
print(f"coin 20 st: {num_020_lv}")
print(f"coin 10 st: {num_010_lv}")
print(f"coin 5 st: {num_005_lv}")
print(f"coin 2 st: {num_002_lv}")
print(f"coin 1 st: {num_001_lv}")


# -------------------- version 4 ----------------------------


# user's input
change = float(input())
change = int(change * 100)


# additional elements
num_2_lv = 0
num_1_lv = 0
num_050_lv = 0
num_020_lv = 0
num_010_lv = 0
num_005_lv = 0
num_002_lv = 0
num_001_lv = 0


# result
while change != 0:
    if change >= 200:
        while change >= 200:
            num_2_lv += 1
            change -= 200
    elif change >= 100:
        while change >= 100:
            num_1_lv += 1
            change -= 100
    elif change >= 50:
        while change >= 50:
            num_050_lv += 1
            change -= 50
    elif change >= 20:
        while change >= 20:
            num_020_lv += 1
            change -= 20
    elif change >= 10:
        while change >= 10:
            num_010_lv += 1
            change -= 10
    elif change >= 5:
        while change >= 5:
            num_005_lv += 1
            change -= 5
    elif change >= 2:
        while change >= 2:
            num_002_lv += 1
            change -= 2
    elif change >= 1:
        while change >= 1:
            num_001_lv += 1
            change -= 1

total = num_2_lv + num_1_lv + num_050_lv + num_020_lv + num_010_lv + num_005_lv + num_002_lv + num_001_lv
print(f"total coins {total}")

# KK added some text and results!
print(f"coin 2 lv: {num_2_lv}")
print(f"coin 1 lv: {num_1_lv}")
print(f"coin 50 st: {num_050_lv}")
print(f"coin 20 st: {num_020_lv}")
print(f"coin 10 st: {num_010_lv}")
print(f"coin 5 st: {num_005_lv}")
print(f"coin 2 st: {num_002_lv}")
print(f"coin 1 st: {num_001_lv}")
