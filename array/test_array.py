from find_missing_number import missing_number_in_array
from find_missing_element import find_missing_set, find_missing_loop

def test_missing_number_in_array():
	assert missing_number_in_array([1,2,3,4,6],6) == 5
	assert missing_number_in_array([1, 2, 3, 4, 6, 7, 9, 8, 10],10) == 5
	assert missing_number_in_array([1, 2, 3, 4, 6, 5, 7, 9, 10],10) == 8
	assert missing_number_in_array([1, 10, 2, 6, 7, 4, 9, 5, 8],10) == 3

def test_find_missing_element():
	assert find_missing_set([4, 12, 9, 5, 6],[4, 9, 12, 6]) == 5
	assert find_missing_loop([4, 12, 9, 5, 6],[4, 9, 12, 6]) == 5
	assert find_missing_loop([4, 12, 9, 5, 6],[4, 9, 5, 6]) == 12
