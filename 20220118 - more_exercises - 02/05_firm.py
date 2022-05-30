# 20220117 - Python Code - Firm
import math

# user input
hrs_needed = int(input())
days_company_has = int(input())
number_people_working_over_time = int(input())

# calculations & results
hrs_company_normal = days_company_has * 8 * 0.9
hrs_company_overtime = days_company_has * number_people_working_over_time * 2
hrs_company_has = hrs_company_normal + hrs_company_overtime

diff = abs(hrs_company_has - hrs_needed)

if hrs_company_has >= hrs_needed:
    print(f"Yes!{math.floor(diff)} hours left.")
else:
    print(f"Not enough time!{math.ceil(diff)} hours needed.")

# Rounding at the "else" statement is not correct in the problem!
# To work fine on Judge it must be math.ceil and not math.floor
