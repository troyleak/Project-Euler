# Find largest prime factor of 600851475143

#! /bin/python

import math

def isFactor(a):
    if a%600851475143==0:
        return True
    else:
        return False

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0)))

def isPrime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(math.sqrt(n))+1, 2):
        if n % x == 0:
            return False
    return True

primeFactors = []

for i in factors(600851475143):
    if isPrime(i)==True:
        print "and it's prime, appending"
        primeFactors.append(i)
        print str(i) + " appended"
    else:
        print str(i) + " is not prime factor"

print primeFactors

# OR this rather clever solution found on ProjectEuler
primes = set([2])
value = 3
number = 317584931803
while value < sqrt(number):
    isPrime = True
    for k in primes:
        if value % k == 0:
            isPrime = False
            value += 2
    if isPrime:
        primes.add(value)
        if number % value == 0:
            print value
            number /= value
print number
