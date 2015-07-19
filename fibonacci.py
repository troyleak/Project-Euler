def fib(n):
	if n == 1:
		return 1
	elif n == 0:
		return 0
	else:
		return fib(n-2) + fib(n-1)

evenPrimes = []

def fibLoop():
	# Returns the highest fibonacci number under 4M
	z = 1
	while fib(z) < 4000000:
		if fib(z)%2==0:
			evenPrimes.append(fib(z))
			print "Added " + str(fib(z)) + " to the list!"
			z = z + 1
#			print "Adding to Array and incrementing z"
		else:
#			print "Odd number, incrementing z"
			z = z + 1
#		print "under 4M"



fibLoop()
print "Subtracting the last number"
evenPrimes.pop
print "from the total..."
print "which gives us... " + str(sum(evenPrimes))
