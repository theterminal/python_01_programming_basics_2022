# 20220215 - Python Code - Combinations of Letters - judge url: https://judge.softuni.org/Contests/Practice/Index/1381#1

range_start_letter = input()
range_end_letter = input()
not_including_letter = input()

range_start_num = ord(range_start_letter)
range_end_num = ord(range_end_letter)
not_including_num = ord(not_including_letter)

counter_printed = 0

# 97 - 122
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
