# 20220210 - Python - Nested Loops
# Note 02 - Prime Number Generator


range_start = int(input("Enter start range number: "))
range_end = int(input("Enter end range number: "))
flag_prime = 'prime'
prime_counter = 0
num_to_print = ''

for num in range(range_start, range_end + 1):
    while True:
        flag_prime = "prime"

        for i in range(2, num):
            if num % i == 0:
                flag_prime = "non prime"

        if flag_prime == "prime" and num > 1:
            num_to_print += (str(num) + ', ')
            prime_counter += 1

        break

print(f'\nThe prime numbers are:\n{num_to_print.strip(", ")}')
print(f"\nAll prime numbers in the range ({range_start} : {range_end}) are {prime_counter}")
