def isPal(num):
	length = len(num)

	k = 0
	while(k < length/2):
		if(num[k] != num[length - 1 - k]):
			return False
		k += 1

	return True


king = 0

for i in range(100, 1000):
	for j in range(i, 1000):
		prod = i*j
		if isPal(str(prod)) and prod > king:
			king = prod

print king





