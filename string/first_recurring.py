def first_recurring(string_):
	array = []

	for i in string_:
		if i in array:
			return i
		array.append(i)
	return None