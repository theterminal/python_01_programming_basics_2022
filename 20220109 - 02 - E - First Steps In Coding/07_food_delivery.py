# 20220108 Python Code - Food Delivery
# judge url: https://judge.softuni.org/Contests/Compete/Index/2424#6
# pastebin url: https://pastebin.com/KYVJ3CdK

# user input
num_chicken_menus = int(input())
num_fish_menus = int(input())
num_vegetarian_menus = int(input())
delivery_lv = 2.50
cost_per_chicken_menu_lv = 10.35
cost_per_fish_menu_lv = 12.40
cost_per_vegetarian_menu_lv = 8.15

# calculations
cost_for_chicken_menus_lv = num_chicken_menus * cost_per_chicken_menu_lv
cost_for_fish_menus_lv = num_fish_menus * cost_per_fish_menu_lv
cost_for_vegetarian_menus_lv = num_vegetarian_menus * cost_per_vegetarian_menu_lv

sub_total_before_desert_lv = cost_for_chicken_menus_lv + cost_for_fish_menus_lv + cost_for_vegetarian_menus_lv
desert_lv = sub_total_before_desert_lv * 0.2

total_lv = sub_total_before_desert_lv + desert_lv + delivery_lv

# output
print(total_lv)
