# 20220205 - Python Code
# Cake

# user input
cake_width = int(input())
cake_length = int(input())

# calculations & results
total_available_pcs = cake_width * cake_length
pcs_entered = 0

while True:
    pcs_entered = input()

    if pcs_entered != "STOP":
        pcs_entered = int(pcs_entered)
        total_available_pcs -= pcs_entered

        if total_available_pcs <= 0:
            print(f"No more cake left! You need {abs(total_available_pcs)} pieces more.")
            break
    else:
        print(f"{total_available_pcs} pieces are left.")
        break
