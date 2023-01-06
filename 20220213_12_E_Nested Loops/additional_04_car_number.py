# 20220215 - Python - Nested Loops
# Additional 04 - Car Number - judge: https://judge.softuni.org/Contests/Practice/Index/1381#3


range_start = range_end = ''

while True:
    range_start = int(input())
    if not(1 <= range_start <= 9):
        print(f'Number entered out of range [1:9]')
        continue
    range_end = int(input())
    if not(1 <= range_start <= 9):
        print(f'Number entered out of range [1:9]')
        continue
    break

for digit_1 in range(range_start, range_end + 1):
    for digit_2 in range(range_start, range_end + 1):
        for digit_3 in range(range_start, range_end + 1):
            for digit_4 in range(range_start, range_end + 1):
                if (digit_1 % 2 == 0 and digit_4 % 2 != 0) or (digit_1 % 2 != 0 and digit_4 % 2 == 0):
                    if digit_1 > digit_4:
                        if (digit_2 + digit_3) % 2 == 0:
                            print(f'{digit_1}{digit_2}{digit_3}{digit_4}', end=' ')
