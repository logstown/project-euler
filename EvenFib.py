def fib(n):

	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return (fib(n-1) + fib(n-2))


tot = 0
n=2
term = 1 
while(term < 4000000):
	if term % 2 == 0:
		tot += term

	n = n+1
	term = fib(n)

print tot
