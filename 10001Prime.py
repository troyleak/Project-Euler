import math
import time
s = time.time()

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

counterList = [2]

for i in xrange (3,999999,2):
    if isPrime(i)==True:
        counterList.append(i)
        if len(counterList)==10001:
            print "10001st prime detected"
            print str(counterList.pop())
            break
print time.time() - s
