# Generates all even fibonacci numbers under 4,000,000 and adds them up

def fib(n):
	if n == 1:
		return 1
	elif n == 0:
		return 0
	else:
		return fib(n-2) + fib(n-1)

def checkEven(x):
	if (x%2==0):
#		print "Even!"
		return True
	else:
#		print "Odd!"
		return False

def checkUnder4M(y):
	if (y<4000000):
		return True
	else:
#		print "over 4M"
		return False


def loopFunction():
	# Returns the highest base number that makes a fibonacci under 4M
	evenPrimes = []
	z = 1
	while checkUnder4M(fib(z)) == True:
		if checkEven(fib(z)) == True:
			evenPrimes.append(fib(z))
			z = z + 1
			print fib(z)
#			print "Adding to Array and incrementing z"
		else:
#			print "Odd number, incrementing z"
			z = z + 1
#		print "under 4M"
	return str(evenPrimes)

loopFunction()
