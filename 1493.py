# 1493. В одном шаге от счастья
# https://acm.timus.ru/problem.aspx?space=1&num=1493
# solved

# simply sum left half and right half
# left number stay same, we manipulate only right number
# tricky part is that sum of digits not always changes same way as number changes (ex: 056019, 001020)
result = 'No'
ticket_num = input()
left_sum = int(ticket_num[0]) + int(ticket_num[1]) + int(ticket_num[2])
right_sum = int(ticket_num[3]) + int(ticket_num[4]) + int(ticket_num[5])

# ex: 015023
if left_sum == right_sum + 1:
    right_num = int(ticket_num[3:])
    right_num_increased = str(right_num + 1)
    right_sum_increased = 0

    for i in range(len(right_num_increased)):
        right_sum_increased += int(right_num_increased[i])

    if left_sum == right_sum_increased:
        result = 'Yes'

# ex: 024034
if left_sum == right_sum - 1:
    right_num = int(ticket_num[3:])
    right_num_decreased = str(right_num - 1)
    right_sum_decreased = 0

    for i in range(len(right_num_decreased)):
        right_sum_decreased += int(right_num_decreased[i])

    if left_sum == right_sum_decreased:
        result = 'Yes'

print(result)