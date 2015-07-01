sum = 2
primes = [2]

for i in range(3,2000000):
	j = 0
	while primes[j] <= (i/primes[j]) and (i % (primes[j]) != 0):
		j += 1

	if i % primes[j] != 0:
		sum += i
		primes.append(i)

print sum
