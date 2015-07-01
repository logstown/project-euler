def prime(n):
	x = 1
	for i in range(0, n):
		x += 1
		while not isPrime(x,2):
			x += 1
	return x

def isPrime(n, m):
	if m > n/2:
		return True
	elif n % m == 0:
		return False
	else:
		return isPrime(n, m+1)

def isPrimei(n):
	i = 2

	while i <= n/2:
		if n % i == 0:
			return False
		i = i+1
	return True



print prime(10)

