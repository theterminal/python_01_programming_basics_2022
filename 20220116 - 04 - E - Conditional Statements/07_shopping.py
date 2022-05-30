# 20220114 - Python Code - Shopping

# user input
budget = float(input())
num_video_cards = int(input())
num_processors = int(input())
num_rams = int(input())

# calculations & results
amount_video_cards = num_video_cards * 250
amount_processors = num_processors * (amount_video_cards * 0.35)
amount_ram = num_rams * (amount_video_cards * 0.1)

total_amount = amount_video_cards + amount_processors + amount_ram

if num_video_cards > num_processors:
    total_amount *= 0.85

diff = abs(budget - total_amount)

if budget >= total_amount:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")
