def bubble_sort(arr):
	for i in range(0,len(arr)):
		for j in range(i+1,len(arr)):
			if arr[i] > arr[j]:
				arr[i],arr[j] = arr[j], arr[i]

	return arr

def merge(left, right):
	result = []
	i,j = 0,0
	while i<len(left) and j < len(right):
		print(left[i],right[j])
		if left[i] < right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	result += left[i:]
	result += right[j:]
	return result
def merge_sort(lst):
	if len(lst) <= 1:
		return lst
	else:
		mid = len(lst)//2
		left = merge_sort(lst[:mid])
		right = merge_sort(lst[mid:])
		return merge(left, right)
