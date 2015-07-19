for i in (2,600851475143):
    if isFactor(i)==True:
        factors.append(i)
        print str(i) + " is a factor" # check isFactor works
        if isPrime(i)==True:
            addToStack(i)
            print str(i) + " is prime" # check isPrime works


def checkExit():
    if d > 600851475143:
        return True
    else:
        return False

def addToStack(c):
    primeFactors.append(c)
    print str(c)

for i in xrange(2,600):
    if factors(i)==True:
        print "found a factor"
        if isPrime(i)==True:
            print "and it's prime, appending"
            primeFactors.append(i)
            print str(i)
        else:
            print str(i) + " is not prime factor"
    else:
        print str(i) + " is not a factor"

def isPrime(b):
    if b == 1:
        print "isPrime returns False - 1 is not prime"
        return False
    elif b == 2:
        print "isPrime returns True - 2 is a prime number"
        return True
    print "greater than 2"
    for z in xrange(3, int(math.sqrt(b)+1), 2):
        # print str(z) + " entering loop"
        if b%z==0:
            print str(z) + " is not a prime number"
            return False
        else:
            print str(z) + " is prime"
            return True

# initializes an empty list to dump potential prime factors in
tempList = []

for i in (1,20):
    tempList.extend(factors(i))

factorList = []

# Removes duplicates by checking how many times each number is in the list.
# Discards any that return more than 0, and 1 and 20 because we don't need those
for i in tempList:
    if (factorList.count(i)==0) and (i!=1) and (i!=20):
        factorList.append(i)
        print "added " + str(i)

product = []

for x in factorList:
    product.append(x)

print str(reduce(prod,product))
_____________________________________________________________________________

def prod(x,y):
    return x*y

def divider(z):
    for i in xrange(1,20):
        if z%i==0:
            print str(z) + " is divisible by " + str(i)
            numberList.append(i)

for x in xrange(1,10000):
    print str(x)
    if isDivisible(x)==True:
        numberList.append(x)
        print str(x)

print str(numberList)


# RETURNS True IF GIVEN NUMBER IS DIVISIBLE BY ALL NUMBERS 1-20
def isDivisible(n):
    # This function right here is giving me shit. Can't figure out how to make
    # it check if n%i==0 for all i in range(1,20)
    if all(n%i==0 for i in range(2,20)):
        print str(n) + " is divisible by all numbers 1-20"
        return True


a = 17
  for x < 100, x++
    a = a + a
    if var a = *[2,4,6,8]0 -> array;

array3 = []
array4 = []
array5 = []
array6 = []
array7 = []
array8 = []
array9 = []
array10 = []
array11 = []
array12 = []
array13 = []
array14 = []
array15 = []
array16 = []
array17 = []
array18 = []
array19 = []
array20 = []
