# 20220219 - Python - Programming Basics - Pre-Exam
# 06 - Sum And Product - judge: https://judge.softuni.org/Contests/Compete/Index/3351#5


# user information
n_number_entered = int(input())


# calculations & results

for a in range(1, 10):
    for b in range(9, a - 1, -1):
        for c in range(0, 10):
            for d in range(9, c - 1, -1):
                abcd_sum = a + b + c + d
                abcd_product = a * b * c * d

                if abcd_sum == abcd_product and n_number_entered % 10 == 5:
                    print(f"{a}{b}{c}{d}")
                    quit()

                if abcd_product // abcd_sum == 3 and n_number_entered % 3 == 0:
                    print(f"{d}{c}{b}{a}")
                    quit()

print(f"Nothing found")
