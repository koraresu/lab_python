from collections import OrderedDict

def first_not_repeating_table(string_):
	table = OrderedDict()
	for i in string_:
		if i in table:
			table[i] += 1
		else:
			table [i] = 1
	for (n,v) in table.items():
		if v == 1:
			return n
def first_not_repeating(string_):
	for i in string_:
		if string_.rindex(i) == string_.index(i):
			return i
# Roate Array Manually
def reverse(array_):
	new_array = [0,]*len(array_)
	y = 0
	i = len(array_)-1
	while y <= len(array_)-1:
		new_array[i] = array_[y]
		y += 1
		i -= 1
	return new_array
def rotate_array_manually(array_):
	array_ = reverse(array_)
	new_array = []
	for x in range(0,len(array_[0])):
		a = []
		for y in range(0,len(array_)):
			a.append(array_[y][x])
		new_array.append(a)
	return new_array
# Rotate Array Using Code
def rotate_array(array_):
	return list(zip(*reversed(array_)))