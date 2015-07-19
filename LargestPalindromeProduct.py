#! /usr/bin/python

palindromes = []
# Find the largest palindrome made from the product of two 3-digit numbers
for x in xrange(0,999):
    for y in xrange(0,999):
        print "checking " + str(x) + " times " + str(y)
        currNum = x*y
        if (str(currNum)==str(currNum)[::-1]):
            palindromes.append(currNum)


print max(palindromes)
