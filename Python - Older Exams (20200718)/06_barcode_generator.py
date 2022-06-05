# 20220218 - Python Code - Barcode Generator - judge url: https://judge.softuni.org/Contests/Practice/Index/2507#5

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


# -----------------------lecture logic-------------------------------------------------

# start = int(input())
# end = int(input())
#
# s1 = start // 1000 % 10
# s2 = start // 100 % 10
# s3 = start // 10 % 10
# s4 = start % 10
#
# print(f"s1 = {s1}")
# print(f"s2 = {s2}")
# print(f"s3 = {s3}")
# print(f"s4 = {s4}")

# -----------------------another version-----------------------------------------------

# Python Code (20220218) - Barcode Generator - https://judge.softuni.org/Contests/Practice/Index/2507#5

# num_1 = input()
# num_2 = input()
#
# s1, s2, s3, s4 = int(num_1[0]), int(num_1[1]), int(num_1[2]), int(num_1[3])
# e1, e2, e3, e4 = int(num_2[0]), int(num_2[1]), int(num_2[2]), int(num_2[3])
#
# for i in (s1, e1 + 1):
#     if i % 2 == 0:
#         continue
#     for j in (s2, e2 + 1):
#         if j % 2 == 0:
#             continue
#         for k in (s3, e3 + 1):
#             if k % 2 == 0:
#                 continue
#             for m in (s4, e4 + 1):
#                 if m % 2 == 0:
#                     continue
#                 print(f"{i}{j}{k}{m}", end=" ")

# ----------------------another version--------------------------------------------

# Python Code - Barcode Generator - https://judge.softuni.org/Contests/Practice/Index/2507#5

# # user input
# num_1 = int(input())
# num_2 = int(input())
#
# # calculations & results
# counter = 0
# i_0_s, i_1_s, i_2_s, i_3_s, = 0, 0, 0, 0
# i_0_e, i_1_e, i_2_e, i_3_e, = 0, 0, 0, 0
# str1 = str(num_1)
# str2 = str(num_2)
# for i, v in enumerate(str1):
#     if i == 0:
#         i_0_s = int(v)
#     elif i == 1:
#         i_1_s = int(v)
#     elif i == 2:
#         i_2_s = int(v)
#     elif i == 3:
#         i_3_s = int(v)
# for i, v in enumerate(str2):
#     if i == 0:
#         i_0_e = int(v)
#     elif i == 1:
#         i_1_e = int(v)
#     elif i == 2:
#         i_2_e = int(v)
#     elif i == 3:
#         i_3_e = int(v)
#
# for i in range(i_0_s, i_0_e + 1):
#     if i % 2 == 0:
#         continue
#     for j in range(i_1_s, i_1_e + 1):
#         if j % 2 == 0:
#             continue
#         for k in range(i_2_s, i_2_e + 1):
#             if k % 2 == 0:
#                 continue
#             for m in range(i_3_s, i_3_e + 1):
#                 if m % 2 == 0:
#                     continue
#                 print(f"{i}{j}{k}{m}", end=" ")
#                 counter += 1
# print()
# print(f"total numbers: {counter}")
