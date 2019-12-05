# 1573. Алхимия
# solved

# reagents amount
reagents_amount = input().split(' ')

# blue
b = int(reagents_amount[0])
# red
r = int(reagents_amount[1])
# yellow
y = int(reagents_amount[2])

# recipe
k = int(input())

result = 1
for i in range(k):
    color = input()

    if color == 'Blue':
        result *= b
    if color == 'Red':
        result *= r
    if color == 'Yellow':
        result *= y

print(result)