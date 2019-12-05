# codeforces round 602 div 2 - A
# solved

t = int(input())

for i in range(t):
    n = int(input())

    if n == 1:
        useless_input = input()
        print(0)
    else:
        separate_ranges = 0

        for j in range(n):
            num_range = input().split(' ')
            l = int(num_range[0])
            r = int(num_range[1])

            if j == 0:
                l_max = l
                r_min = r
            else:
                if l_max <= l <= r_min or l_max <= r <= r_min or l <= l_max <= r or l <= r_min <= r:
                    separate_ranges = separate_ranges
                else:
                    separate_ranges += 1

                if l > l_max:
                    l_max = l
                if r < r_min:
                    r_min = r

        if separate_ranges == 0:
            print(0)
        else:
            result = abs(r_min - l_max)
            print(result)