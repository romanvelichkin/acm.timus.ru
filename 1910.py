# 1910. Руины титанов: сокрытый вход
# solved

sections_num = int(input())
sections_list = input().split(' ')

max_power_sum = 0
max_power_mid_num = 0
mid_num = 0

for i in range(len(sections_list) - 2):
    power_sum = 0

    for j in range(3):
        power_sum = power_sum + int(sections_list[i+j])
        if j == 1:
            mid_num = i+j + 1
    if power_sum > max_power_sum:
        max_power_sum = power_sum
        max_power_mid_num = mid_num

print(str(max_power_sum) + ' ' + str(max_power_mid_num))