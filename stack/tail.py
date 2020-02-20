def get_tail(file, n):
	stack = []
	with open(file, "r") as f:
		for line in f:
			if len(stack) >= n:
				stack.pop(0)
			stack.append(line)
	return stack