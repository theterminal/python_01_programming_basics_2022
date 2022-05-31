# 20220130 - Python Code
# Bills

# user's input
num_months = int(input())

# additional elements
electric_bill = 0
total_electric = 0
other = 0
sum_other = 0

# calculations
for i in range(num_months):
    electric_bill = float(input())
    total_electric += electric_bill
    other = (electric_bill + 35) * 1.2
    sum_other += other

bill_water = num_months * 20
bill_internet = num_months * 15
average_monthly = (total_electric + bill_water + bill_internet + sum_other) / num_months

# result
print(f"Electricity: {total_electric:.2f} lv")
print(f"Water: {bill_water:.2f} lv")
print(f"Internet: {bill_internet:.2f} lv")
print(f"Other: {sum_other:.2f} lv")
print(f"Average: {average_monthly:.2f} lv")
