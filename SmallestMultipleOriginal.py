import math

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0)))

def product(x,y):
    return x*y

## Checks if z is an element of iterable and returns True if it is.
def isElement(z, iterable):
    iterable = list(iterable)
    if iterable.count(z)==0:
        print str(z) + " is not an element of " + str(iterable)
        return False
    else:
        return True

def isPrime(n):
    '''check if integer n is a prime'''
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(math.sqrt(n))+1, 2):
        if n % x == 0:
            return False
    return True

finalList = []
checkList = [11,13,14,16,17,18,19,20]

def findSolution(num):
    for num in xrange(num, 999999999, num):
        if all(num % n == 0 for n in checkList):
            print str(num)
            return num

print str(findSolution(2520))
