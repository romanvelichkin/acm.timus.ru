# 1581. Работа в команде
# solved

n = int(input())
nums = input().split(' ')
result = ''
current_num = ''
current_num_times = 0

for i in range(n):
    if current_num != nums[i]:
        if current_num_times != 0:
            result = result + ' ' + str(current_num_times) + ' ' + current_num
            current_num_times = 0
        current_num = nums[i]
        current_num_times = 1
    else:
        current_num_times += 1

result = result + ' ' + str(current_num_times) + ' ' + current_num

print(result[1:])