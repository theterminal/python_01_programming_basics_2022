# 20220114 - Python - Programming Basics - Conditional Statements
# 08 - Lunch Break


# user input
import math

movie_name = input()
length_movie_min = int(input())
break_time_min = int(input())


# calculations & results
time_to_eat = break_time_min * 0.125
time_to_relax = break_time_min * 0.250
movie_time = break_time_min - (time_to_eat + time_to_relax)

diff = abs(movie_time - length_movie_min)

if movie_time >= length_movie_min:
    print(f"You have enough time to watch {movie_name} and left with {math.ceil(diff)} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {math.ceil(diff)} more minutes.")
