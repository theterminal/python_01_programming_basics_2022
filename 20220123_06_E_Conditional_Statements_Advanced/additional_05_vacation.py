# 20220123 - Python - Conditional Statements Advanced
# additional 05 - Vacation


# user input
budget = float(input())
season = input().lower()


# calculations & results
sleep_at = ""
location = ""
price = 0

if budget <= 1000:
    sleep_at = "Camp"
    if season == "summer":
        location = "Alaska"
        price = budget * 0.65
    elif season == "winter":
        location = "Morocco"
        price = budget * 0.45
elif 1000 < budget <= 3000:
    sleep_at = "Hut"
    if season == "summer":
        location = "Alaska"
        price = budget * 0.8
    elif season == "winter":
        location = "Morocco"
        price = budget * 0.6
elif budget > 3000:
    sleep_at = "Hotel"
    price = budget * 0.9
    if season == "summer":
        location = "Alaska"
    elif season == "winter":
        location = "Morocco"

print(f"{location} - {sleep_at} - {price:.2f}")
