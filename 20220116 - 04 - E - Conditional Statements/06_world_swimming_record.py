# 20220114 - Python Code - World Swimming Record

# user input
old_record_sec = float(input())
distance_to_swim_m = float(input())
time_for_1_m_sec = float(input())
resistance_15_m_sec = 12.5

# calculations & results
time_for_distance = distance_to_swim_m * time_for_1_m_sec
resistance = distance_to_swim_m // 15 * 12.5
total_time = time_for_distance + resistance

diff = abs(total_time - old_record_sec)

if old_record_sec <= total_time:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
