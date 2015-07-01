def seq(n):
	if n == 1:
		return 1
	if n % 2 == 0:
		return 1 + seq(n/2)

	return 1 + seq(3*n+1)

longestLength = 0

for i in range(1, 1000000):
	chain = seq(i)
	if chain > longestLength:
		longestLength = chain
		king = i

print king