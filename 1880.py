# 1880. Собственные числа Psych Up

a_amount = int(input())
a_numbers = set(input().split(' '))

b_amount = int(input())
b_numbers = set(input().split(' '))

c_amount = int(input())
c_numbers = set(input().split(' '))

if a_amount > b_amount:
    a_b_same = a_numbers - a_numbers.difference(b_numbers)
else:
    a_b_same = b_numbers - b_numbers.difference(a_numbers)

if b_amount > c_amount:
    b_c_same = b_numbers - b_numbers.difference(c_numbers)
else:
    b_c_same = c_numbers - c_numbers.difference(b_numbers)

if len(a_b_same) > len(b_c_same):
    a_b_c_same = a_b_same - a_b_same.difference(b_c_same)
else:
    a_b_c_same = b_c_same - b_c_same.difference(a_b_same)

print(len(a_b_c_same))


