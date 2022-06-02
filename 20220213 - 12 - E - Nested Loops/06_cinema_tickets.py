# 20220210 - Python Code - Cinema Tickets

# user input
name_of_movie_entered = input()

# calculations & results
counter_total, counter_student, counter_standard, counter_kid = 0, 0, 0, 0

while name_of_movie_entered != "Finish":
    seats_all_entered = int(input())
    seats_available = seats_all_entered
    tickets_sold_this_movie = 0

    while seats_available > 0:
        ticket_type_entered = input()

        if ticket_type_entered == "End":
            break
        elif ticket_type_entered == "student":
            counter_student += 1
        elif ticket_type_entered == "standard":
            counter_standard += 1
        elif ticket_type_entered == "kid":
            counter_kid += 1

        seats_available -= 1
        tickets_sold_this_movie += 1
        counter_total += 1

    percent_sold = tickets_sold_this_movie / seats_all_entered * 100
    print(F"{name_of_movie_entered} - {percent_sold:.2f}% full.")
    name_of_movie_entered = input()

# result
if counter_total == 0:
    print(F"Total tickets: 0")
    print(F"0.00% student tickets.")
    print(F"0.00% standard tickets.")
    print(F"0.00% kids tickets.")
else:
    print(F"Total tickets: {counter_total}")
    print(F"{(counter_student / counter_total * 100):.2f}% student tickets.")
    print(F"{(counter_standard / counter_total * 100):.2f}% standard tickets.")
    print(F"{(counter_kid / counter_total * 100):.2f}% kids tickets.")
