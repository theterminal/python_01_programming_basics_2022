# 20220218 - Python Code - Agency Profit

# user's input
airline_name = input()
num_tickets_adults = int(input())
num_tickets_kids = int(input())
price_ticket_adult = float(input())
fee_ticket = float(input())

# calculations
price_ticket_kid = price_ticket_adult * 0.3

sales_tickets_adults = num_tickets_adults * (price_ticket_adult + fee_ticket)
sales_tickets_kids = num_tickets_kids * (price_ticket_kid + fee_ticket)
sales_total = sales_tickets_adults + sales_tickets_kids
profit = sales_total * 0.2

# result
print(f'The profit of your agency from {airline_name} tickets is {profit:.2f} lv.')
