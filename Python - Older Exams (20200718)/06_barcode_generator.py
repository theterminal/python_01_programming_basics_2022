# 20220218 - Python Code - Barcode Generator

range_start = input()
range_end = input()

for digit_1 in range(int(range_start[0]), int(range_end[0]) + 1):
    if digit_1 % 2 == 0:
        continue

    for digit_2 in range(int(range_start[1]), int(range_end[1]) + 1):
        if digit_2 % 2 == 0:
            continue

        for digit_3 in range(int(range_start[2]), int(range_end[2]) + 1):
            if digit_3 % 2 == 0:
                continue

            for digit_4 in range(int(range_start[3]), int(range_end[3]) + 1):
                if digit_4 % 2 == 0:
                    continue

                print(f'{digit_1}{digit_2}{digit_3}{digit_4}', end=" ")
