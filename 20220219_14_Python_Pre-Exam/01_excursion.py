# 20220219 - Python - Programming Basics - Pre-Exam
# 01 - Excursion - judge: https://judge.softuni.org/Contests/Compete/Index/3351#0


# user information
num_people_in_the_group_entered = int(input())
num_nights_entered = int(input())
num_cards_entered = int(input())
num_tickets_museum = int(input())
cost_per_night_per_person = 20
cost_per_card_per_person = 1.60
cost_per_ticket_museum_per_person = 6


# calculations & results
cost_per_person_for_nights = num_nights_entered * cost_per_night_per_person
cost_total_for_cards = num_cards_entered * cost_per_card_per_person
cost_total_for_tickets = num_tickets_museum * cost_per_ticket_museum_per_person

total_one_person = cost_per_person_for_nights + cost_total_for_cards + cost_total_for_tickets

total_cost = total_one_person * num_people_in_the_group_entered
total_cost *= 1.25

print(f"{total_cost:.2f}")
