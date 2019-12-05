# 1197. Один в поле воин

tests_amount = int(input())
list_result = []

while tests_amount > 0:
    input_data = input()
    letter = input_data[:1]
    num = int(input_data[1:])

    result = 8

    if letter in ('b', 'g'):
        result = result - 2
    if letter in ('a', 'h'):
        result = result - 4

    if result > 6:
        if num in (2, 7):
            result = result - 2
        if num in (1, 8):
            result = result - 4

    elif result > 4:
        if num in (2, 7):
            result = result - 2
        if num in (1, 8):
            result = result - 3

    elif result <= 4:
        if num in (2, 7):
            result = result - 1
        if num in (1, 8):
            result = result - 2

    list_result.append(result)

    tests_amount = tests_amount - 1

for i in range(len(list_result)):
    print(list_result[i])

