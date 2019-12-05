# 1608. Счастливые билеты 2008

# 100-999 unlucky tickets
"""
counter = 0
for i in range(100, 1000):
    num = str(i)

    same_num = 0
    for j in range(len(num) // 2):
        if num[j] == num[len(num) - j-1]:
            same_num = 1

    if same_num == 1:
        counter += 1

print(str(counter))
"""

"""
#1-9 and 10-99
unlucky_dict = {1:0, 2:9}
unlucky_amount = 0

for i in range(3, 19):
    if i%2 == 1:
        unlucky_amount = unlucky_dict.get(i-1) * 10
    else:
        unlucky_amount = 90 * (unlucky_dict.get(i-2) + 10**(i-3))
    unlucky_dict[i] = unlucky_amount

print(unlucky_dict)

input_data = input().split(' ')
a = input_data[0]
b = input_data[1]
unlucky_in_a = 0
unlucky_in_b = 0
for i in range(len(b)):
    #print('i=' + str(i) + ' ' + 'b[i]=' + b[i] + ' ' + 'len(b)-i=' + str(len(b)-i))
    # exclude max i
    # range between 1 and 10**(len(b))-1, if 1234, then its 1-999
    if i < len(b) - 1:
       unlucky_in_b = unlucky_in_b + unlucky_dict.get(len(b)-i - 1)
    # range between 10**(len(b)) and b, if 1234, then its 1000-1234
    if i < len(b) - 1:
        unlucky_in_b = unlucky_in_b + unlucky_dict.get(len(b) - i - 1)

print(unlucky_in_b)

result = (b-a) - (unlucky_in_b - unlucky_in_a)
"""

# works for 1-9 - 10000-99999, doesn't work for 100000-999999
num = str(input())
counter = 0
for i in range(len(num) // 2):
    if i == 0:
        # first and last
        counter = 9 * 10**(len(num) - 2)
        #for j in range(len(num)//6):
        #if len(b) > 5:
        #    print(str(9 * 9 * 10**(len(num) - 4)))
        #    counter = counter - 9 * 9 * 10**(len(num) - 4)
    else:
        # all other digits
        counter = counter + 10*9 * 10**(len(num) - 3)
        #for j in range (len(num)//2 - (len(num)//2 - 1)):
        #    print(str(9 * 10**(len(num) - 3)))
         #   counter = counter - 9 * 10**(len(num) - 3)

print(str(10**(len(num) - 1)) + '-' + num + ' = ' + str(counter))