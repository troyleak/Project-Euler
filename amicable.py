#!/usr/bin/env python3

"""
Amicable numbers
Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are

1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.

The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import math

# returns a list of divisors of a number
def divisorGenerator(n):
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                yield n / i

# returns sum of divisors of a number
def d(n):
    return sum(divisorGenerator(n))

def find_amicable_pairs():
    amicable_pairs = []
    for a in range(1, 10000):
        # if str(a) in [j for i in amicable_pairs for j in i]:
        #     break
        b = d(a)
        # if d(a) > 10000 or d(b) > 10000:
        #     break
        if d(b) == a:
            amicable_pairs.append([int(a), int(b)])
    return amicable_pairs

result = find_amicable_pairs()
print(result)
result = map(sum, result)
print(sum(result))
