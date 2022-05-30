# 20220117 - Python Code - Sleepy Cat Tom

# user input
number_days_off = int(input())
min_norm_year = 30000

# calculations & results
min_days_off = number_days_off * 127
min_days_on = (365 - number_days_off) * 63
min_total_year = min_days_on + min_days_off

diff = abs(min_total_year - 30000)
h_diff = diff // 60
min_diff = diff % 60

if min_total_year > min_norm_year:
    print(f"Tom will run away")
    print(f"{h_diff} hours and {min_diff} minutes more for play")
else:
    print(f"Tom sleeps well")
    print(f"{h_diff} hours and {min_diff} minutes less for play")
