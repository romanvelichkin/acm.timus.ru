# 1100
# solved

# use dictionary to solve this problem
# m (amount of solved problems) will be keys, id (team num) will be items
# fill dictionary, create list of keys and sort it, then print keys and items
# do not convert teams' ids into strings, it takes too much time


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        sorted_array = []

        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                sorted_array.append(left.pop(0))
            else:
                sorted_array.append(right.pop(0))

        for i in left:
            sorted_array.append(i)
        for i in right:
            sorted_array.append(i)

    else:
        sorted_array = array

    return sorted_array


n = int(input())

input_dict = {}

for i in range(n):
    input_data = input().split(' ')
    team = input_data[0]
    problems_amount = int(input_data[1])

    teams_with_problems_amount = []

    if problems_amount in input_dict.keys():
        teams_with_problems_amount = input_dict[problems_amount]

    teams_with_problems_amount.append(team)
    input_dict[problems_amount] = teams_with_problems_amount

input_dict_keys = merge_sort(list(input_dict.keys()))

for i in range(len(input_dict_keys))[::-1]:
    problems_amount = input_dict_keys[i]
    teams_with_problems_amount = input_dict[problems_amount]

    for j in range(len(teams_with_problems_amount)):
        print(teams_with_problems_amount[j], problems_amount)