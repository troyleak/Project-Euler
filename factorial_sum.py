#!/usr/bin/env python3

"""
Project Euler Problem 20

Usage: call the script with a number

Description:
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""
import sys

def factorial(n):
    n = int(n)
    if n == 1:
        return 1
    else:
        return (int(n) * factorial(int(n) - 1))

def add_sum(n):
    result=0
    for i in str(n):
        result += int(i)
    return result

print(add_sum(factorial(sys.argv[1])))
