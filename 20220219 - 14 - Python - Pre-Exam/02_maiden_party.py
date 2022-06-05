# 20220219 - Python Code - Maiden Party - judge url: https://judge.softuni.org/Contests/Compete/Index/3351#1

# user information
money_needed_bgn = float(input())
num_love_entered = int(input())
num_roses_entered = int(input())
num_keychains_entered = int(input())
num_caricatures_entered = int(input())
num_surprises_entered = int(input())

price_per_love, price_per_rose, price_per_keychain, price_per_caricature, price_per_surprise = 0.60, 7.20, 3.60, 18.20, 22.00

# calculations & results
amount_love_bgn = num_love_entered * price_per_love
amount_roses_gbn = num_roses_entered * price_per_rose
amount_keychains_bgn = num_keychains_entered * price_per_keychain
amount_caricatures_bgn = num_caricatures_entered * price_per_caricature
amount_surprises_bgn = num_surprises_entered * price_per_surprise

total_bgn = amount_love_bgn + amount_roses_gbn + amount_keychains_bgn + amount_caricatures_bgn + amount_surprises_bgn
total_items = num_love_entered + num_roses_entered + num_keychains_entered + num_caricatures_entered + num_surprises_entered

if total_items >= 25:
    total_bgn *= 0.65

total_bgn *= 0.9

diff = abs(total_bgn - money_needed_bgn)

if total_bgn >= money_needed_bgn:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
