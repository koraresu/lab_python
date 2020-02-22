from mathematics import prime, fib, fib_array
from sum import sum_loop, check_nearest
def test_prime():
	assert prime(100) == False
	assert prime(7) == True
	assert prime(2) == True
	assert prime(49) == False
	assert prime(10) == False
	assert prime(1) == False


def test_fib():
	assert fib(1) == 0
	assert fib(2) == 1
	assert fib(3) == 1
	assert fib(4) == 2
	assert fib(5) == 3
	assert fib(6) == 5
	assert fib(7) == 8
	assert fib(8) == 13
	assert fib(9) == 21
	assert fib(10) == 34
	assert fib(11) == 55

def test_fib_array():
	assert fib_array(1)  == [0]
	assert fib_array(2)  == [0, 1]
	assert fib_array(3)  == [0, 1, 1]
	assert fib_array(4)  == [0, 1, 1, 2]
	assert fib_array(5)  == [0, 1, 1, 2, 3]
	assert fib_array(6)  == [0, 1, 1, 2, 3, 5]
	assert fib_array(7)  == [0, 1, 1, 2, 3, 5, 8]
	assert fib_array(8)  == [0, 1, 1, 2, 3, 5, 8, 13]
	assert fib_array(9)  == [0, 1, 1, 2, 3, 5, 8, 13, 21]
	assert fib_array(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
	assert fib_array(11) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def test_sum():
	assert sum_loop([1,2,3,4,5,6,7,8,9,10],12) == [(3, 9), (4, 8), (5, 7)]
	assert sum_loop([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],18) == [(0, 18), (1, 17), (2, 16), (3, 15), (4, 14), (5, 13), (6, 12), (7, 11), (8, 10)]
def test_check_nearest():
	assert check_nearest([1,2,3,4,5,6,7,8,9,13], 12) == 13
	assert check_nearest([1,2,3,4,5,6,7,8,9,11], 12) == 11