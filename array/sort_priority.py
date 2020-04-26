from operator import itemgetter

def sort_strings_priority(list_):
	list_.sort(key=itemgetter(0,1,2))
	print(list_)

