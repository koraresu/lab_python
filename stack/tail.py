import os

def get_tail(file, n=10000):
	stack = []
	with open(file, 'r') as f:

		for line in f:
			line = str(line).replace("\n","")
			if len(stack) >= n:
				stack.pop(0)
			stack.append(line)
	return stack