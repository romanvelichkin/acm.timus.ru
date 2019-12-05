# codeforces round 600 div 2 - A
# solved

t = int(input())

for i in range(t):
    n = int(input())
    a_list = input().split(' ')
    b_list = input().split(' ')

    prev_diff = 0
    current_diff = 0
    diff_found = 0
    result = ''

    if n == 1:
        if b_list[0] >= a_list[0]:
            result = 'YES'
        else:
            result = 'NO'
    else:
        for j in range(n):
            current_diff = int(b_list[j]) - int(a_list[j])

            if current_diff < 0:
                result = 'NO'
            else:
                if diff_found == 0:
                    if current_diff != 0:
                        prev_diff = current_diff
                        diff_found = 1
                else:
                    if current_diff == 0:
                        prev_diff = current_diff
                    else:
                        if prev_diff == 0:
                            result = 'NO'
                        if prev_diff != 0 and prev_diff != current_diff:
                            result = 'NO'

    if result == '':
        result = 'YES'

    print(result)



#1
#3
#1 2 3
#2 2 4
