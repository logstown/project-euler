# Starting in the top left corner of a 22 grid, and only being able to move to the right and down, 
# there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 2020 grid?


def path(x,y):

	if x ==0 or y==0:
		return 1

	return path(x-1,y) + path(x,y-1)


def path2(x):
	if x == 0:
		return 1

	return path2(x-1) + path2(x-1)

def fact(n):

	if n==0:
		return 1;

	return n * fact(n-1)


# print path(10,10)

n = 20
k = 20
print fact(n+k-1)/(fact(n-1)*fact(k)) *2

# print fact(4)



