# 1209. 1, 10, 100, 1000...
# solved

"""
1 10 100 1000 10000 100000
0 1  3   6    10    15

10**0 = 0 position
10**1 = 1 position (+1 position)
10**2 = 3 position (+2 positions)
10**3 = 6 position (+3 positions)
10**4 = 10 position (+4 positions)
10**5 = 15 position (+5 positions)

We can see here progression:
X(n) = X(n-1) + n
where X(n) - position of Nth digit '1'

We can expand it:
X(n) = X(n-1) + n = (X(n-2) + n-1) + n = ((X(n-3) + n-2) + n-1) + n = (((X(n-4) + n-3) + n-2) + n-1) + n
X(n) = X(n-1) + n = X(n-2) + 2*n - = X(n-3) + 3*n - 3 = X(n-4) + 4*n - 6

where 1 can be written as X(1), 3 is X(2), 6 as X(3) etc

Now we can write formula for it:
X(n) = X(n-y) + y*n - X(y-1)

So if y = n then it will look like this:
X(n) = X(n-n) + n*n - X(n-1) = n*n - X(n-1)

We can write X(n-1) as X(n) - n:
X(n) = n*n - (X(n) - n)
2*X(n) = n*n + n

Then final formula is:
X(n) = (n*n + n) / 2

2*X(n) = n*n + n is a square equation:
a*n*n + b*n + c = 0

In this case:
a = 1
b = 1
c = -2 * X(n)

Solution will be:
d = b*b - 4*a*c = 1 + 8*X(n)
n = sqrt(d)-b / 2*a = (sqrt(8*X(n) + 1) - 1) / 2

As we see all 'n' are integer numbers, so we need to check it
if it's integer then there is '1' digit, otherwise '0'


In program X(n) is named as 'k'
"""

import math

n = int(input())
result = ''

for i in range(n):
    k = int(input()) - 1  # My numbers start from 0 not 1
    x = (math.sqrt(k * 8 + 1) - 1) / 2

    if int(x) == x:
        result = result + '1 '
    else:
        result = result + '0 '

print(result)