#!/usr/bin/env python3

"""
Work out the first ten digits of the sum of the following
one-hundred 50-digit numbers.

numbers in .dat file in same directory
"""

n = [int(line.rstrip('\n')) for line in open('fifty_digit_numbers.dat', 'r')]

n = sum(n)
print(str(n)[:10])
