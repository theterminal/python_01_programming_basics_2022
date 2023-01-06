# 20220215 - Python - Nested Loops
# Additional 05 - Challenge The Wedding - judge: https://judge.softuni.org/Contests/Practice/Index/1381#4


num_customers_men = int(input())
num_customers_women = int(input())
num_tables_max = int(input())

counter_tables, flag = 0, 0

for i in range(1, num_customers_men + 1):
    for j in range(1, num_customers_women + 1):
        counter_tables += 1

        if counter_tables > num_tables_max:
            flag = 1
            break
        print(f'({i} <-> {j})', end=" ")

    if flag:
        break
