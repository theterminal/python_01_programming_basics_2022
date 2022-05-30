# Python Code -

# user input
num_juniors = int(input())
num_seniors = int(input())
track_type = input()

# calculations & results
amount_juniors = 0
amount_seniors = 0

if track_type == "trail":
    amount_juniors = num_juniors * 5.50
    amount_seniors = num_seniors * 7
elif track_type == "cross-country":
    amount_juniors = num_juniors * 8
    amount_seniors = num_seniors * 9.5
    if (num_juniors + num_seniors) >= 50:
        amount_juniors *= 0.75
        amount_seniors *= 0.75
elif track_type == "downhill":
    amount_juniors = num_juniors * 12.25
    amount_seniors = num_seniors * 13.75
elif track_type == "road":
    amount_juniors = num_juniors * 20
    amount_seniors = num_seniors * 21.50

total_amount = amount_juniors + amount_seniors
total_amount *= 0.95

print(f"{total_amount:.2f}")
