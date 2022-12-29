# 20220121 - Python - Conditional Statements Advanced
# 08 - On Time For The Exam


# user input
exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())


# calculations & results
exam = exam_hour * 60 + exam_minutes
arr = arrival_hour * 60 + arrival_minutes

diff = abs(exam - arr)
h_print = diff // 60
m_print = diff % 60

if 0 <= diff <= 30 and arr <= exam:
    print("On time")
    if diff > 0:
        print(f"{m_print} minutes before the start")
elif arr < exam:
    print("Early")
    if diff < 60:
        print(f"{m_print} minutes before the start")
    else:
        print(f"{h_print}:{m_print:02d} hours before the start")
else:
    print("Late")
    if diff < 60:
        print(f"{m_print} minutes after the start")
    elif diff != 0:
        print(f"{h_print}:{m_print:02d} hours after the start")
