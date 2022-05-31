# 20220130 - Python Code
# Logistics

# user's input
number_loads = int(input())

# additional elements
tons_bus = tons_truck = tons_train = 0
paid_bus = paid_truck = paid_train = 0

# calculations
for i in range(number_loads):
    weight_load_ton = int(input())

    if weight_load_ton <= 3:
        tons_bus += weight_load_ton
        paid_bus = tons_bus * 200
    elif weight_load_ton <= 11:
        tons_truck += weight_load_ton
        paid_truck = tons_truck * 175
    elif weight_load_ton >= 12:
        tons_train += weight_load_ton
        paid_train = tons_train * 120

total_tons = tons_bus + tons_truck + tons_train
total_paid = paid_bus + paid_truck + paid_train
average_price_per_ton = total_paid / total_tons

percent_tons_bus = tons_bus / total_tons * 100
percent_tons_truck = tons_truck / total_tons * 100
percent_tons_train = tons_train / total_tons * 100

# result
print(f'{average_price_per_ton:.2f}')
print(f'{percent_tons_bus:.2f}%')
print(f'{percent_tons_truck:.2f}%')
print(f'{percent_tons_train:.2f}%')
