#!/usr/bin/env python3

"""
1000-digit Fibonacci number
Problem 25
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000
digits?
"""

# This solution provides a good compromise between memory and CPU efficiency
# The recursive function below could also find the answer, but recomputing the
# values below the n we want will use a lot of unnecessary computing power

# def fib(n):
#     if n < 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# A better way is to store the intermediate numbers in an array and address the
# end with a negative index. However, since the last two numbers are all that's
# necessary to create the next one, we can have values after f(n-2) fall off the
# end to save space. This makes for a very tidy and fast algorithm.

f = [1, 1, 0]

def is_under_1000_digits(n):
    return (len(str(n)) < 1000)

# start at one because we're given the first digit.
# add one because PE indexes at 1 for some dumb reason.
index = 2
while True:
    if is_under_1000_digits(f[0]):
        f[2] = f[1]
        f[1] = f[0]
        f[0] = f[1] + f[2]
        index += 1
    else:
        print(index)
        break
