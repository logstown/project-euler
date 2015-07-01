import math

def triangle(n):
	return (n * (n+1)) / 2

def divi(tri):

	div = 0
	i = 1

	while i < int(math.sqrt(tri)):
		if tri % i == 0:
			div += 2
		i += 1

	if i == int(math.sqrt(tri)):
		div += 1


	return div





n = 1
div = 1

while div <= 500:
	n += 1
	tri = triangle(n)
	div = divi(tri)

print tri


# 1: 1
# 3: 1,3
# 6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# 36: 1,2,3,4,6,9,12,18,36
