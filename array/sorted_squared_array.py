def sorted_squared_array(arr):
	new_arr = []
	for i in range(0, len(arr)):
		res = arr[i]*arr[i]
		if len(new_arr) >= 1:
			for j in range(0, len(new_arr)):
				if new_arr[j] > res:
					new_arr = new_arr[0:j] + [res] + new_arr[j:len(new_arr)]
					break
		else:
			new_arr.append(res)
	return new_arr