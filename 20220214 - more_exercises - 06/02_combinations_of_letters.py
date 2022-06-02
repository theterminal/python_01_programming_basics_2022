# 20220215 - Python Code - Combinations of Letters - judge url: https://judge.softuni.org/Contests/Practice/Index/1381#1

range_start_num = ord(input())
range_end_num = ord(input())
not_including_num = ord(input())

counter_printed = 0

for i in range(range_start_num, range_end_num + 1):
    if i == not_including_num:
        continue

    for j in range(range_start_num, range_end_num + 1):
        if j == not_including_num:
            continue

        for k in range(range_start_num, range_end_num + 1):
            if k == not_including_num:
                continue

            print(f'{chr(i)}{chr(j)}{chr(k)}', end=" ")
            counter_printed += 1

print(counter_printed)
