def fact(n):
	if n == 0:
		return 1
	else:
		return n * fact(n-1)

tot = 0
nums = str(fact(100))

for i in range(0, len(nums)):
	tot += int(nums[i])

print tot