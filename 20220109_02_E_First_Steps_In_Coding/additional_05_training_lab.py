# 20220111 - Python - Programming Basics
# additional 05 - Training Lab - judge: https://judge.softuni.org/Contests/Practice/Index/1642#4
# pastebin: https://pastebin.com/LERqAB8q


# user input
length_m = float(input())
width_m = float(input())
walkway_width_cm = 100


# calculations
length_cm = length_m * 100
width_cm = width_m * 100

num_workspaces_per_width = (width_cm - walkway_width_cm) // 70
num_workspaces_per_length = length_cm // 120

total_workspaces = int((num_workspaces_per_width * num_workspaces_per_length) - 3)


# output
print(f"{total_workspaces}")


# -------------- older solution --------------------------------------------------------


# given information
one_work_space_sq_cm = 8400
walkway_cm = 100


# user's input
length_m = float(input())
width_m = float(input())


# calculations
width_cm = width_m * 100
length_cm = length_m * 100

useful_width_cm = width_cm - walkway_cm

desks_per_width = useful_width_cm // 70
columns = length_cm // 120

total_workspaces = desks_per_width * columns - 3


# result
print('{:.{}f}'.format(total_workspaces, 0))
