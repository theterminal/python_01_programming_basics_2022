# 20220111 Python Code - Fish Land
# judge url: https://judge.softuni.org/Contests/Practice/Index/1642#5
# pastebin url: https://pastebin.com/qpt82JYu

# user input
price_mackerel_lv_per_kg = float(input())
price_sprat_lv_per_kg = float(input())
bonito_kg = float(input())
horse_mackerel_kg = float(input())
mussels_kg = int(input())
price_mussels_lv_per_kg = 7.50

# calculations
price_bonito_lv_per_kg = price_mackerel_lv_per_kg * 1.6
price_horse_mackerel_lv_per_kg = price_sprat_lv_per_kg * 1.8

cost_bonito_lv = bonito_kg * price_bonito_lv_per_kg
cost_horse_mackerel_lv = horse_mackerel_kg * price_horse_mackerel_lv_per_kg
cost_mussels_lv = mussels_kg * price_mussels_lv_per_kg

total_ordered_lv = cost_bonito_lv + cost_horse_mackerel_lv + cost_mussels_lv

# output
print(f'{total_ordered_lv:.2f}')
