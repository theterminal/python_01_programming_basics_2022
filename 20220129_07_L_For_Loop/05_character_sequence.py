# 20220128 - Python - For Loop
# 05 - Character Sequence - judge: https://judge.softuni.org/Contests/Compete/Index/2417#4


text_entered = input()

for i in text_entered:
    print(i)
    # print(i, end="")                     # to print on one line


# ------- loop using index of str -------------------------------


text_entered = input()

for i in range(len(text_entered)):
    print(text_entered[i])


# ------- printing the index of char before the char ------------


text_entered = input()
j = 0

for i in text_entered:
    print(j, end=" ")
    print(text_entered[j])
    j += 1
