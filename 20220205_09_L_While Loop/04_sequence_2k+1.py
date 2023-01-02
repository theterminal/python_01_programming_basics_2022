# 20220130 - Python - While Loop
# 04 - Sequence "2k + 1" - judge: https://judge.softuni.org/Contests/Compete/Index/2419#3


# user input
num_test = int(input())


# calculations & results
num_entered = 1

while num_entered <= num_test:
    print(num_entered)
    num_entered *= 2 + 1
