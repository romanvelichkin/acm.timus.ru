# 1876. Утро сороконожки
# solved

boots = input().split(' ')
left_boots = int(boots[0])
right_boots = int(boots[1])
left_legs = 40
right_legs = 40
result = 0

if right_boots >= left_boots:
    result = right_boots*2 + left_legs
else:
    result = (right_legs - 1)*2 + left_legs + (left_boots - left_legs)*2 + 1
print(result)