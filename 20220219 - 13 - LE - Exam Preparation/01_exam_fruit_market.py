# Python Code - Fruit Market - https://judge.softuni.org/Contests/Practice/Index/1654#0

# user input
price_strawberry_bgn = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberry_kg = float(input())
strawberry_kg = float(input())

# calculations & results
price_raspberry_bgn = price_strawberry_bgn * 0.5
price_oranges_bgn = price_raspberry_bgn * 0.6
price_bananas_bgn = price_raspberry_bgn * 0.2

amount_bananas_bgn = bananas_kg * price_bananas_bgn
amount_oranges_bgn = oranges_kg * price_oranges_bgn
amount_raspberry_bgn = raspberry_kg * price_raspberry_bgn
amount_strawberry_bgn = strawberry_kg * price_strawberry_bgn

total_gbn = amount_bananas_bgn + amount_oranges_bgn + amount_raspberry_bgn + amount_strawberry_bgn

print(f"{total_gbn:.2f}")
