# 1991. Битва у болота
# solved

input_data_d = input().split(' ')
n = int(input_data_d[0])
k = int(input_data_d[1])

input_data_g = input().split(' ')

droids_alive = 0
unused = 0

for i in range(n):
    fight_result = k - int(input_data_g[i])

    if fight_result > 0:
        droids_alive += fight_result
    elif fight_result < 0:
        unused += abs(fight_result)

print(unused, droids_alive)
