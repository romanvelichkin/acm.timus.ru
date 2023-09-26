# 1607. Такси
# https://acm.timus.ru/problem.aspx?space=1&num=1607

# solved

# tricky part is when to check price and order of steps
# there could be used an arithmetic progression,
# but without understanding order of steps and price check it will be pure guessing

input_str = input().split(' ')
petya_price = int(input_str[0])
petya_step = int(input_str[1])
taxi_price = int(input_str[2])
taxi_step = int(input_str[3])

result = 0
price_found = False

# if petya price bigger than drive price from start, somehow petya price is correct
# I guess it's because driver didn't tell his price yet and agreed on petya options
if petya_price >= taxi_price:
    result = petya_price
    price_found = True

while not price_found:
    # petya won't name price bigger than driver named
    if petya_price < taxi_price and not price_found:
        if petya_price + petya_step >= taxi_price:
            result = taxi_price
            price_found = True
        else:
            petya_price += petya_step

    # driver won't name price lesser than petya named
    if taxi_price > petya_price and not price_found:
        if taxi_price - taxi_step <= petya_price:
            result = petya_price
            price_found = True
        else:
            taxi_price -= taxi_step

print(result)