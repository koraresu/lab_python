import sys

def sum_loop(arr, n):
	array = []
	for i in range(0,len(arr)-1):
		for j in range(i+1, len(arr)-1):
			if arr[i] + arr[j] == n:
				array.append((arr[i],arr[j]))
	return array

def check_nearest(arr, n):
	# x = sys.maxsize
	# last_i = 0
	# for i in range(0,len(arr)):
	# 	v = abs(arr[i]-n)
	# 	if x > v:
	# 		x = v
	# 		last_i = i
	# return arr[last_i]
	return min(arr, key=lambda x: abs(x-n))

