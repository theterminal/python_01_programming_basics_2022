# 20220128 - Python - For Loop
# 03 - Even Powers - judge: https://judge.softuni.org/Contests/Compete/Index/2417#2


# ---------- version 2 -----------------------


n = int(input())

for i in range(0, n + 1, 2):
    # number = pow(2, i)            # method 1
    number = 2 ** i                 # method 2
    print(number)


# ---------- version 1 -----------------------


# user's input
n = int(input())

num = 1

# result
for power in range(0, n + 1, 2):
    # print(pow(2, power))
    # --------------------
    print(2 ** power)
    # --------------------
    # print(num)
    # num = num * 2 * 2
    # --------------------
