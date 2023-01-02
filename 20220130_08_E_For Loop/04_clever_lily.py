# 20220129 - Python - For Loop
# 04 - Clever Lily - judge: https://judge.softuni.org/Contests/Compete/Index/2418#3


age = int(input())
washer = float(input())
toy_price = int(input())

sum_odd, counter_toys, counter_money = 0, 0, 1

for i in range(1, age + 1):
    if i % 2 != 0:
        counter_toys += 1
    else:
        b_day_money = counter_money * 10 - 1
        sum_odd += b_day_money
        counter_money += 1

money_toys = counter_toys * toy_price
total_money = sum_odd + money_toys

diff = f"{abs(total_money - washer):.2f}"

if total_money >= washer:
    print(f"Yes! {diff}")
else:
    print(f"No! {diff}")
