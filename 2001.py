# 2001. Математики и ягоды

# комбинации из ягод и корзин
combo_1 = input().split(' ')
combo_2 = input().split(' ')
combo_3 = input().split(' ')

a1 = int(combo_1[0])
b1 = int(combo_1[1])
a2 = int(combo_2[0])
b2 = int(combo_2[1])
a3 = int(combo_3[0])
b3 = int(combo_3[1])

berries_1 = a1 - a3
berries_2 = b1 - b2

print(str(berries_1) + ' ' + str(berries_2))

