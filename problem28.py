
x = 1
incr = 0
tot = 0

while x < 1002002:
	
	tot += x
	

	if (x / (incr+1) == (incr+1)) and (x % (incr+1) == 0):
		incr += 2


	x += incr

print tot

		

			

