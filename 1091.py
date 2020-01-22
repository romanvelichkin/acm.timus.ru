# 1091. Tmutarakan Exams
# solved

"""
We need to use combinatorics to solve this problem.

Problem says we need to find all unique combinations
for numbers which have common divisor.

It limits us: max possible divisor with full combination equals S//K,
so we need to find combinations for all divisors between 2 and S//K.

Formula for number of possible combinations is: n! / m!*(n-m)!,
where n - total number of items, m - items in combination (size).

Some combinations can be similar for different divisors. Ex.: 2 (8 16) and 4 (8 16)
So we have to use only prime number.
But even with prime number we can have similar combinations.
This happens if S >= prime_a * prime_b * k. Ex.: S=12, k=2, a=2 (6 12) and b=3 (6 12)

We can find amount of numbers that can be used for same combinations
by diving S on prime numbers: Z = S // prime_a // prime_b
We search for same combinations using previous formula: z! / z!*(n-z)!
and then subtract them from result.

We need to search same combinations just for two prime divisors,
because minimal possible S with three prime divisors is 60:
S=60, k=2, a=2 (30, 60) and b=3 (30, 60) and c=5 (30,60),
while we can have maximum possible S equal 50.
"""

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return (fact)


def find_prime_numbers(r):
    prime_numbers_list = [2]
    if r > 2:
        for i in range(3, r + 1):
            prime = 1
            for j in prime_numbers_list:
                if i % j == 0:  # can be divided so number is not prime
                    prime = 0
                    break
            if prime == 1:
                prime_numbers_list.append(i)
    return(prime_numbers_list)


data = input().split(' ')
k = int(data[0])
s = int(data[1])
result = 0

max_divisor = s // k
prime_numbers_list = find_prime_numbers(max_divisor)

for i in prime_numbers_list:
    m = s // i  # how many numbers has this divisor
    x = factorial(m) / (factorial(k) * factorial(m - k))
    result += x

same_comb = 0
for x in range(len(prime_numbers_list)):
    for y in range(x + 1, len(prime_numbers_list)):
        prime_a = prime_numbers_list[x]
        prime_b = prime_numbers_list[y]

        if s >= prime_a * prime_b * k:
            z = s // prime_a // prime_b
            same_comb += factorial(z) / (factorial(k) * factorial(z - k))

result = result - same_comb

if result > 10000:
    result = 10000

print(int(result))