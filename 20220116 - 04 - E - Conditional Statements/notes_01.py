# 20220114 - Python Code

a = float(input('Enter a number => a = '))
b = float(input('Enter a number => b = '))

c = a / b
d = a // b
e = a % b
f = d * b + e

print(f'Result c => (a / b) => (c = {c})')
print(f'Result d => (a // b) => (d = {d})')
print(f'Result e => (a % b) => (e = {e})')
print(f'Result f => reconstruction of \'a\' => (d * b + e) => (f = {f:.0f})')
