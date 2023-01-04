# 20220208 - Python - Nested Loops
# Note 01 - TOTO 6 from 49 All Combinations Printed


# given information
num_cycle = 0


# calculations & result
for i in range(1, 50):
    for j in range(1, 50):
        for k in range(1, 50):
            for l in range(1, 50):
                for m in range(1, 50):
                    for n in range(1, 50):
                        num_cycle += 1
                        print(f"{i}, {j}, {k}, {l}, {m}, {n}; combination # {num_cycle}")
