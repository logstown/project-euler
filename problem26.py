king = {'num': 0, 'length': 0}

for x in range(11,1000):
	nums = []

	if x < 100:
		newNum = 10
	else:
		newNum = 100

	while(newNum not in nums and newNum != 0):
		nums.append(newNum)
		newNum = newNum*10 % x

	if newNum != 0:
		length = len(nums) - nums.index(newNum)
		if length > king['length']:
			king = {'num': x, 'length': length}

	if x == 13:
		print length

print king


