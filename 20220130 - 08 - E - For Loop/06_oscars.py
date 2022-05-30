# 20220129 - Python Code
# Oscars

actor_name = input()
points_academy = float(input())
judges = int(input())

points_sum = total_points = 0

for i in range(judges):
    judge_name = len(input())
    current_judge_points = float(input())
    current_judge_total_points = (current_judge_points * judge_name) / 2
    points_sum += current_judge_total_points
    total_points = points_academy + points_sum

    if total_points >= 1250.5:
        break

diff = f"{abs(1250.5 - total_points):.1f}"

if total_points >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {diff} more!")

# --------------another way of showing the result--------------------------

# # Python Code - Oscars
#
# # user input
# actor_name = input()
# points_academy = float(input())
# judges = int(input())
#
# # calculations & results
# point_sum = 0
# total_points = 0
#
# for i in range(judges):
#     name = len(input())
#     points = (float(input()) * name) / 2
#     point_sum += points
#     total_points = points_academy + point_sum
#
#     if total_points >= 1250.5:
#         print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
#         quit()
#
# diff = f"{abs(1250.5 - total_points):.1f}"
# print(f"Sorry, {actor_name} you need {diff} more!")

