# 1044. Lucky Tickets. Easy!
# solved

import math

digits = int(input())/2
result = 0
counts_half = (digits*9 + 1)/2

if math.floor(counts_half) == counts_half:
    counts_even = 1
else:
    counts_even = 0

count_till = math.floor(counts_half)

for i in range(count_till - counts_even + 1):

    combinations = 0

    if digits == 1:
        combinations += 1
    else:
        if i <= 9:
            max_num = i
        else:
            max_num = 9

        for j in range(max_num + 1):
            if digits == 2:
                combinations += 1
            else:
                if i - j < max_num:
                    k_max = i - j
                else:
                    k_max = max_num

                for k in range(k_max + 1):
                    if digits == 3:
                        if i - j - k <= 9:
                            combinations += 1
                    else:
                        if i - j - k < max_num:
                            l_max = i - j - k
                        else:
                            l_max = max_num

                        for l in range(l_max + 1):
                            if i - j - k - l <= 9:
                                combinations += 1

    if i == count_till and counts_even == 0:
        result += combinations ** 2
    else:
        result += combinations ** 2 * 2

print(result)
