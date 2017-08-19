#!/usr/bin/env python3

"""
Project Euler Problem 16

Usage: call the script with a number

Description:
2^15 = 32,768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1,000?
"""

import sys

def power_of_two(n):
    result = pow(2, int(n))
    # print(result)
    return result

def add_sum(n):
    result=0
    for i in str(n):
        result += int(i)
        # print(result)
    return result

print(add_sum(power_of_two(sys.argv[1])))
