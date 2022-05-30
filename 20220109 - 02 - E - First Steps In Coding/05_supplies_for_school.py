# 20220109 - Python Code - Supplies For School
# judge url: https://judge.softuni.org/Contests/Compete/Index/2424#4
# pastebin url: https://pastebin.com/XQHPZRHb

# user input
num_pens_packs, num_markers_packs, cleaner_l, discount_percent = int(input()), int(input()), int(input()), int(input())
cost_pens_lv_per_pack = 5.80
cost_markers_lv_per_pack = 7.20
cost_cleaner_lv_per_l = 1.20

# calculations
cost_all_pens_lv = num_pens_packs * cost_pens_lv_per_pack
cost_all_markers_lv = num_markers_packs * cost_markers_lv_per_pack
cost_all_solution_lv = cleaner_l * cost_cleaner_lv_per_l
sub_total_lv = cost_all_pens_lv + cost_all_markers_lv + cost_all_solution_lv

# output
discount_lv = sub_total_lv * (discount_percent / 100)
total_lv = sub_total_lv - discount_lv

# Output
print(f"{total_lv}")
