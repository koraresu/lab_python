def first_duplicate(arr):
	arr_duplicate = []
	for i in range(1,len(arr)):
		if arr[abs(arr[i])-1] < 0:
			arr_duplicate.append(arr[i]) 
		arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]  
	return arr_duplicate