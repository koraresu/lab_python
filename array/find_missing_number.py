def missing_number_in_array(arr, n):
	valid_list = [i for i in range(1,n)]

	for i in valid_list:
		if i not in arr:
			return i
