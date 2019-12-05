# 1893. A380

# A1-2 - window
# B1-2 - aisle
# C1-2 - aisle
# D1-2 - window

# 1-2 A-D A, D - window
# 3-20 A-F A, F - window
# 21-65 A-K A, K - window

#AB CD EF
#ABC DEFG HJK

place = input()
num_pos = len(place) - 1
number = int(place[:num_pos])
letter = place[num_pos:]

if number >= 21:
    if letter == 'C' or letter == 'D' or letter == 'G' or letter == 'H':
        result = 'aisle'
    else:
        result = 'neither'
elif number >= 3:
    if letter == 'F':
        result = 'window'
    else:
        result = 'aisle'
elif number >= 1:
    if letter == 'B' or letter == 'C':
        result = 'aisle'
    else:
        result = 'window'

if letter == 'A':
    result = 'window'
if letter == 'K':
    result = 'window'


print(result)