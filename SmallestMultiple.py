# Smallest Multiple
# The problem can be simplified to the product of the common prime factors of
# all numbers 1-20
import time
s = time.time()

checkList = [11,13,14,16,17,18,19,20]

def findSolution(num):
    for num in xrange(num, 999999999, num):
        if all(num % n == 0 for n in checkList):
            print str(num)
            return num

print str(findSolution(2520))
print "Completed in " + str(time.time() - s) + " seconds"
