
def pfacts(n, m):
	if m == 1:
		print 1
	elif n % m == 0:
		print n/m
		pfacts(m, m/2)
	else:
		pfacts(n, m-1)

def prime(n,m):
	if m == 1:
		return n
	elif n % m == 0:
		return prime(m, m/2)
	else:
		return prime(n, m-1)

def another(n, m):
	if m > n/2:
		return n
	elif n % m == 0:
		return another(n/m, m)
	else:
		return another(n, m+1)

def another1(n, i):
	while( i <= n/2):
		if n % i == 0:
			return another1(n/i, i)
		i = i+1
	return n



def iterative( n ):
	i = n/2

	while(i>0):
		if isPrime(i) and (n%i == 0):
			return(i)
		i = i-1

	return n


def isPrime( n ):

    if n < 2:
        return False
    else:
    	for i in range(2, n/2):
            if n % i == 0:
                return False  

    return True


# pfacts(130,130/2)
# print iterative(600851475143)
# print another(35,2)
print another1(600851475143,2)
# print prime(13195, 13195/2)
# print prime(13195, 13195/2)