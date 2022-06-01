# # 20220208 - Python Code - Sum of Two Numbers

# user input
num_start = int(input())
num_end = int(input())
num_magic = int(input())

# calculations & results
counter_magic = 0

for i in range(num_start, num_end + 1):
    for j in range(num_start, num_end + 1):
        counter_magic += 1
        if i + j == num_magic:
            print(f"Combination N:{counter_magic} ({i} + {j} = {num_magic})")
            exit()

print(f"{counter_magic} combinations - neither equals {num_magic}")
