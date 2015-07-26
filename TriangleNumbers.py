# HIGHLY DIVISIBLE TRIANGULAR NUMBER
# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

# 1: 1
# 3: 1,3
# 6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28

# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?
import math
import time
s = time.time()

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0)))
# Going to reuse the factors function from previously

def triangularNumbers(n):
    return sum(range(n))
# This function takes a number as an index and returns the triangular number at
# that index

finalList = []

for i in xrange(5,50000):
    finalList.append(triangularNumbers(i))
# Builds a list of triangular numbers

for x in finalList:
    if (len(factors(x)) > 500):
        print x
        break

# Currently this program takes forever to run (and 99% CPU time), probably
# having to do with
# calculating every factor. Implementing a binary search algorithm should speed
# things up.

# Also only need to check the triangular numbers
print "Completed in " + str(time.time() - s) + " seconds"