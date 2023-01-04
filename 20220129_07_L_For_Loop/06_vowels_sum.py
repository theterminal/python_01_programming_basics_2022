# 20220128 - Python - For Loop
# 06 - Vowels Sum - judge: https://judge.softuni.org/Contests/Compete/Index/2417#5


word = input()
total = 0

for i in word:
    if i == "a":
        total += 1
    elif i == "e":
        total += 2
    elif i == "i":
        total += 3
    elif i == "o":
        total += 4
    elif i == "u":
        total += 5

print(f"{total}")
