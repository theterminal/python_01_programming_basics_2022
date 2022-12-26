# 20220117 - Python - Programming Basics - Conditional Statements
# additional 01 - Pipes In a Pool


# user input
volume_pool_l = int(input())
p1_l_per_h = int(input())
p2_l_per_h = int(input())
hours = float(input())


# calculations & results
l_p1 = p1_l_per_h * hours
l_p2 = p2_l_per_h * hours
total_filled_l = l_p1 + l_p2

percent_p1_from_total_filled_l = l_p1 / total_filled_l * 100
percent_p2_from_total_filled_l = l_p2 / total_filled_l * 100
percent_total = total_filled_l / volume_pool_l * 100
overflow_l = total_filled_l - volume_pool_l

if volume_pool_l >= total_filled_l:
    print(f"The pool is {percent_total:.2f}% full. Pipe 1: {percent_p1_from_total_filled_l:.2f}%. Pipe 2: {percent_p2_from_total_filled_l:.2f}%.")
else:
    print(f"For {hours:.2f} hours the pool overflows with {overflow_l:.2f} liters.")
