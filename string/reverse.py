
def reverse_while(string_):
	print(string_)
	i = len(string_)-1
	output = ''
	while i >= 0:
		output += string_[i]
		i = i - 1
	return output

def reverse_slicing(string_):
	return string_[::-1]

def reverse_using_loop(string_):
	output = ''
	for i in string_:
		output = i + output
	return output
