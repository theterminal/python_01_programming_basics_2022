# 20220109 - Python - Programming Basics
# 06 - Repainting - judge: https://judge.softuni.org/Contests/Compete/Index/2424#5
# pastebin: https://pastebin.com/VZ5bAUL9


# user input
plastic_needed_sq_m = int(input())
paint_needed_l = int(input())
paint_thinner_needed_l = int(input())
work_needed_hrs = int(input())

cost_of_bags_lv = 0.40
cost_of_plastic_lv_per_sq_m = 1.50
cost_of_paint_lv_per_l = 14.50
cost_of_thinner_lv_per_l = 5.00


# calculations
plastic_needed_sq_m += 2
paint_needed_l *= 1.1
cost_of_plastic_lv = plastic_needed_sq_m * cost_of_plastic_lv_per_sq_m
cost_of_paint_lv = paint_needed_l * cost_of_paint_lv_per_l
cost_of_thinner_lv = paint_thinner_needed_l * cost_of_thinner_lv_per_l
cost_of_materials_lv = cost_of_plastic_lv + cost_of_paint_lv + cost_of_thinner_lv + cost_of_bags_lv

cost_of_work_lv_per_hr = cost_of_materials_lv * 0.3
total_work_lv = cost_of_work_lv_per_hr * work_needed_hrs

total_cost_lv = cost_of_materials_lv + total_work_lv


# output
print(f"{total_cost_lv}")
