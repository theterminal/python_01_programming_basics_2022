# Python Code - Time + 15 minutes

# user input
hours = int(input())
minutes = int(input())

# calculations & results
hrs_to_minutes = hours * 60
total_minutes = hrs_to_minutes + minutes + 15

end_hour = total_minutes // 60
if end_hour == 24:
    end_hour = 0
end_minutes = total_minutes % 60

print(f"{end_hour}:{end_minutes:02d}")
