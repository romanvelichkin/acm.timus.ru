# 2149. Принцип Дирихле
# https://acm.timus.ru/problem.aspx?space=1&num=2149

# solved

# main idea is to code doves with 0 and 1 depending on how turned their head
# also alteration score is easy to calculate using numbers

# get all input data
doves_total = int(input())
doves_heads = input()
doves_bodies = input()
doves_legs = input()

doves_list = []
doves_counter = 0

# analysis of doves_heads string (left turned heads coded as 0, right as 1)
while doves_counter < doves_total:
    # get first symbol and cut string by it
    symbol = doves_heads[0]
    doves_heads = doves_heads[1:]

    # head turned right, we save it, cut string one symbol more
    if symbol == '@':
        doves_list.append(1)
        doves_heads = doves_heads[1:]
        doves_counter += 1
        # calc sums for doves halves

    # head turned left, we save it, cut string one symbol more
    if symbol == '<':
        doves_list.append(0)
        doves_heads = doves_heads[1:]
        doves_counter += 1
        # calc sums for doves halves

# <@ <@ @> @> - 0 0 1 1 - same halves one
# @> @> <@ <@ - 1 1 0 0 - same halves two
doves_left_sum = 0
doves_right_sum = 0
# <@ @> <@ @> - 0 1 0 1 - alteration one
alter_score_one = 0
# @> <@ @> <@ - 1 0 1 0 - alteration two
alter_score_two = 0
dove_num = 0

for dove in doves_list:
    dove_num += 1

    # calculate doves score for left half
    if dove_num <= doves_total/2:
        doves_left_sum += dove
    # calculate doves score for right half
    else:
        doves_right_sum += dove

    # odd dove
    if dove_num % 2 != 0:
        # dove head is turned left - 0
        if dove == 0:
            # we need to turn this head to get alteration two
            alter_score_two += 1
        # dove head is turned right - 1
        elif dove == 1:
            # we need to turn this head to get alteration one
            alter_score_one += 1
    # even dove
    elif dove_num % 2 == 0:
        # dove head is turned left - 0
        if dove == 0:
            # we need to turn this head to get alteration one
            alter_score_one += 1
        # dove head is turned right - 1
        elif dove == 1:
            # we need to turn this head to get alteration two
            alter_score_two += 1

# <@ <@ @> @> - 0 0 1 1 - same halves one
# change left half to 0 (turn left) and right half to 1 (turn right)
left_right_score_one = int(doves_left_sum + (doves_total/2 - doves_right_sum))
# @> @> <@ <@ - 1 1 0 0 - same halves two
# change left half to 1 (turn right) and right half to 0 (turn left)
left_right_score_two = int((doves_total/2 - doves_left_sum) + doves_right_sum)

result = min(left_right_score_one, left_right_score_two, alter_score_one, alter_score_two)
print(result)