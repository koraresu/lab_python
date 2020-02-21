# A prime number is any whole number with exactly two factors one and itself, ex: 2, 7, 31
# Write a function that returns whether a non-zero positive integer (>0) is prime (true/false)
# 100 =>   1, 2 , 4, 5, 10, 20, 25, 50, 100 # this is not a prime number (aka composite) 
# 7 => 1, 7                                 # this is a prime number
# 2 => 1, 2                                 # prime
# 49 => 1, 7, 49                            # not prime (composite)
# 10 => 1, 2, 5, 10                         # not prime (composite)
# 1 => 1                                    # not prime (composite) “exactly two factors”
 
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