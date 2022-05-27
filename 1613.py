# 1613 Для любителей статистики
# solved


def binary_seach(array, search_value):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if search_value == array[mid]:
            return 0, search_value
        elif search_value < array[mid]:
            right = mid - 1
        elif search_value > array[mid]:
            left = mid + 1
    # we need first bigger value than search_value
    # if search_value wasn't found then left value will actually bigger (it's left <= right)
    return 1, array[left]


result = ''
n = int(input())
rides_in_cities_input = input().split(' ')
rides_by_cities_dict = {}

# we create dict with rides, with list of cities per each amount of rides
# we fill dict in default order so each list of cities will be sorted
for i in range(n):
    rides = int(rides_in_cities_input[i])
    cities_list = []

    if rides in rides_by_cities_dict.keys():
        cities_list = rides_by_cities_dict[rides]

    cities_list.append(i + 1)
    rides_by_cities_dict[rides] = cities_list

q = int(input())

# now we search if there are city in list that can be found in input range
for i in range(q):
    data_to_search = input().split(' ')
    left_city = int(data_to_search[0])
    right_city = int(data_to_search[1])
    x = int(data_to_search[2])

    if x not in rides_by_cities_dict.keys():
        result += '0'
    else:
        cities_list = rides_by_cities_dict[x]

        left_city_dict = cities_list[0]
        right_city_dict = cities_list[len(cities_list) - 1]

        if left_city <= right_city_dict and right_city >= left_city_dict:

            res, city_num = binary_seach(cities_list, left_city)

            if res == 0:
                result += '1'
            else:
                if city_num <= right_city:
                    result += '1'
                else:
                    result += '0'

        else:
            result += '0'

print(result)

