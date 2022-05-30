# 20220109 Python Code - Basketball Equipment
# judge url: https://judge.softuni.org/Contests/Compete/Index/2424#7
# pastebin url: https://pastebin.com/SDxDvKqy

# user input
yearly_fee = int(input())

# calculations
cost_of_shoes = yearly_fee * 0.6
cost_of_cloths = cost_of_shoes * 0.8
cost_of_ball = cost_of_cloths * 0.25
cost_of_accessories = cost_of_ball * 0.2
sub_total = cost_of_shoes + cost_of_cloths + cost_of_ball + cost_of_accessories
total = sub_total + yearly_fee

# output
print(f"{total}")
