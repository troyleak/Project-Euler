# Pythagorean Triplets
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import time
s = time.time()

for x in xrange(1,300):
    for y in xrange(300,400):
        for z in xrange(400,500):
            if ((x*x)+(y*y)==(z*z)):
                if (x+y+z==1000):
                    print str(x*y*z)
                    break

print "Completed in " + str(time.time() - s) + " seconds"
