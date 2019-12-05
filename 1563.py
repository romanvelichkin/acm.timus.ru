# 1563

n = int(input())
shops = []
counter = 0

for i in range(n):
    shop = input()
    if shop in shops:
        counter = counter + 1
    else:
        shops.append(shop)

print (counter)