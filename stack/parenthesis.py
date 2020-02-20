class Stack:
	def __init__(self):
		self.stack_arr = []
	def is_empty(self):
		return len(self.stack_arr) == 0
	def not_empty(self):
		return len(self.stack_arr) > 0
	def add(self,element):
		self.stack_arr.append(element)
	def pop(self):
		self.stack_arr.pop()
	def last(self):
		return self.stack_arr[len(self.stack_arr)-1]
	def clean(self):
		self.stack_arr.clear()

def check_bracket(string_):
	open_list = ['(', '[']
	close_list = [')', ']']
	valid = 0
	stack = Stack()
	for i in string_:
		if i in open_list:
			stack.add(i)
		elif i in close_list:
			pos = close_list.index(i)
			if stack.not_empty() and open_list[pos] == stack.last():
				stack.pop()
				valid += 2
	return valid