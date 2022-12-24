# 20220109 - Python - Programming Basics
# 04 - Vacation Books - judge: https://judge.softuni.org/Contests/Compete/Index/2424#3
# pastebin: https://pastebin.com/mxmrt3yp


# user input
num_pages_in_book = int(input())
num_pages_read_in_1_hour = int(input())
num_days_to_read_the_book = int(input())


# calculations
num_hrs_for_the_book = num_pages_in_book // num_pages_read_in_1_hour
num_hrs_per_day = num_hrs_for_the_book // num_days_to_read_the_book


# output
print(f"{num_hrs_per_day}")


# -------- The following is another way to get 100% from the judge system because of the decimal point ---------


number_pages_in_a_book = int(input("Enter number of pages in the book: "))
pages_per_hour_read = int(input("Enter how many pages per hour he/she can reed: "))
days_to_read_1_book = int(input("Enter how many days he/she has to read the book: "))

hours_needed_for_the_book = number_pages_in_a_book / pages_per_hour_read
hours_to_read_each_day = hours_needed_for_the_book / days_to_read_1_book

result = int(hours_to_read_each_day)
print(f'He/she has to read every day for {result} hours, so the book can be finished')
