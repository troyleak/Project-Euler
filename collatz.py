#!/usr/bin/env python3

"""
Longest Collatz sequence
Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def collatz(n):
    # returns the next number in the collatz sequence
    if n%2 == 0:
        n = n/2
    else:
        n = (n * 3) + 1
    return n

count = 1

collatz_chain = []

# iterate one million times
for n in range(1000000):
    # The actual Collatz sequence happens here
    while int(n) > 1:
        n = collatz(n)
        count += 1
    # Store the chain in our array for later parsing
    collatz_chain.append(count)
    count = 0

print(collatz_chain.index(max(collatz_chain)))
