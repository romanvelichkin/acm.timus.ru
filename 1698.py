# 1698. Квадратная страна 5
# solved

"""
Checking every number will take O(10**n) iterations.

The very first combination will be:
1*1 = 1

There are just two digits can have squares ending with same digits: 5 and 6.
5*5 = 25
6*6 = 36
So we need to process just numbers that ends with 5 and 6.
Fast test with loops for n = 3 proves it, so we can start proceed.
This improves time to O(2 * 10**(n-1)) iterations.

For n = 8 there will be 15 numbers (and squares for them):
1 1
5 25
6 36
25 625
76 5776
376 141376
625 390625
9376 87909376 
90625 8212890625
109376 11963109376
890625 793212890625
2890625 8355712890625
7109376 50543227109376
12890625 166168212890625
87109376 7588043387109376

We can see every next number is same as previous but with additional digits.
We can use it, so we'll to proceed much less numbers.

This will take maximum O((n-1)*9*2)) operations
Comparing square with number is faster with % than with string slicing

Then you read about automorphic numbers and found:
5th numbers squares let us calculate next automorphic number:
90625 * 90625 = 8212890625, 890625 is automorphic
6th numbers squares let us calculate next automorphic number:
6 * 6 = 36,  10 - 3 = 7, 76 is automorphic
However in both cases we need to deal with 0s and skip them until we find non-zero digit.
Ex: 625 * 625 = 390625, and we can't take 0625, we need to take 90625.
Same works with 6th: 9376 * 9376 = 87909376, and we can't do 10-0 (looks like we can, be it won't work on double zero),
so we need to calculate 100-90.

This solution takes 0.9-0.5 sec for n=2000 in PyCharm
However my code isn't executed fast enough on acm.timus.ru and got exceeded time limit every time.
I contacted support, let's see what they will answer.
So to be accepted you need to precalcuate all solutions for n between 1500 and 2000.
"""

n = int(input())
result = 3

nums = [5, 6]

x = 0
y = 0

if n == 1:
    print(result)
else:
    while x == 0 or y == 0:
        # 5
        m = nums[0]
        sqr_m = m * m
        m_str = str(m)
        sqr_m_str = str(sqr_m)
        len_diff = len(sqr_m_str) - len(m_str) - 1

        j = 0
        digit = sqr_m_str[len_diff:len_diff + 1]

        while digit == '0':
            j += 1
            digit = sqr_m_str[len_diff - j:len_diff - j + 1]
        
        next_five = sqr_m_str[len_diff - j:]

        if len(next_five) <= n:
            nums[0] = int(next_five)
            result += 1
        else:
            x = 1

        # 6
        m = nums[1]
        sqr_m = m * m
        m_str = str(m)
        sqr_m_str = str(sqr_m)
        len_diff = len(sqr_m_str) - len(m_str) - 1

        j = 0
        digit = sqr_m_str[len_diff:len_diff + 1]
        num_calc = digit

        while digit == '0':
            j += 1
            digit = sqr_m_str[len_diff - j:len_diff - j + 1]
            num_calc = digit + num_calc

        next_six = str(10 ** len(num_calc) - int(num_calc)) + m_str

        if len(next_six) <= n:
            nums[1] = int(next_six)
            result += 1
        else:
            y = 1

    print(result)
