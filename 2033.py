# 2033. Девайсы
# solved

n = 6
devices_dict = {}

for i in range(0, n):
    friend_name = input()
    device_name = input()
    device_price = int(input())
    if device_name not in devices_dict:
        devices_dict[device_name] = [1, device_price]
    else:
        devices_dict[device_name][0] += 1
        if device_price < devices_dict[device_name][1]:
            devices_dict[device_name][1] = device_price

devices_max_amount = 0
best_device = ''
cheapest_device = 0

for i in devices_dict:
    if devices_dict[i][0] > devices_max_amount:
        devices_max_amount = devices_dict[i][0]
        cheapest_device = devices_dict[i][1]
        best_device = i
    elif devices_dict[i][0] == devices_max_amount and devices_dict[i][1] < cheapest_device:
        cheapest_device = devices_dict[i][1]
        best_device = i

print(best_device)




