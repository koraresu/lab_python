def prime(n):
	if n == 1:
		return False
	for i in range(2, n):
		if n % i == 0:
			return False
	return True

def fib(n):
	a = [0, 1,1]
	if n <= 3:
		return a[0:n][-1]
	for i in range(3,n):
		a.append(a[-2]+a[-1])
		if len(a) >= 2:
			a.pop(0)
	return a[-1]

def fib_array(n):
	a = [0,1,1]
	if n <= 3:
		return a[0:n]
	for i in range(3,n):
		a.append(a[-2]+a[-1])
	return a

