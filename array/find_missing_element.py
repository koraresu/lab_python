# find_missing(
#    [4, 12, 9, 5, 6],
#    [4, 9, 12, 6]
# )


def find_missing_set(arr, arr2):
	missing_items = set(arr) - set(arr2)
	if len(missing_items) == 0:
		return False
	else:
		return list(missing_items)[0]

def find_missing_loop(arr, arr2):
	for i in arr:
		if i not in arr2:
			return i
