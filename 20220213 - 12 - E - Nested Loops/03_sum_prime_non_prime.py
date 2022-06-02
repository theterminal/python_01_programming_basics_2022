# 20220210 - Python Code - Sum Prime Numbers and Non Prime Numbers

sum_nums_prime, sum_nums_non_prime, flag = 0, 0, False

while True:
    num_entered = input()

    if num_entered == "stop":
        break

    num_entered = int(num_entered)

    if num_entered < 0:
        print("Number is negative.")
        continue

    for i in range(2, num_entered):
        if num_entered % i == 0:
            sum_nums_non_prime += num_entered
            flag = True
            break

    if not flag:
        sum_nums_prime += num_entered

    flag = False

print(f"Sum of all prime numbers is: {sum_nums_prime}")
print(f"Sum of all non prime numbers is: {sum_nums_non_prime}")
