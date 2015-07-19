tempArray = []
finalArray = []
testArray = [1,1,1,1,1,1,1,1,1]

def isRepeated(n):
    if tempArray.count(n)>9:
        return True
    else:
        return False

for x in xrange(2520,1000000,20):
    for i in range(11,20):
        print "Trying " + str(x)
        if (x%i==0):
            tempArray.append(x)
        else:
            break

tempArray = filter(isRepeated,tempArray)
testArray = filter(isRepeated,testArray)
print str(testArray)
print str(tempArray)
print str(finalArray)
