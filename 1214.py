# 1214. Странная процедура
# solved

# loop in this task does one thing - swaps x and y
# so we check if it has even or odd amount of cycles
input_data = input().split(' ')

x = int(input_data[0])
y = int(input_data[1])

if (x+y) % 2 != 0 and x > 0 and y > 0:
    print(str(y) + ' ' + str(x))
else:
    print(str(x) + ' ' + str(y))
