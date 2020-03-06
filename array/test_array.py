from find_missing_number import missing_number_in_array
from find_missing_element import find_missing_set, find_missing_loop
from sort_problem import bubble_sort,merge_sort
from find_first_duplicate import first_duplicate
from sorted_squared_array import sorted_squared_array
from no_repeating import rotate_array_manually,rotate_array
from no_repeating import first_not_repeating_table,first_not_repeating

def test_missing_number_in_array():
	assert missing_number_in_array([1,2,3,4,6],6) == 5
	assert missing_number_in_array([1, 2, 3, 4, 6, 7, 9, 8, 10],10) == 5
	assert missing_number_in_array([1, 2, 3, 4, 6, 5, 7, 9, 10],10) == 8
	assert missing_number_in_array([1, 10, 2, 6, 7, 4, 9, 5, 8],10) == 3

def test_find_missing_element():
	assert find_missing_set([4, 12, 9, 5, 6],[4, 9, 12, 6]) == 5
	assert find_missing_loop([4, 12, 9, 5, 6],[4, 9, 12, 6]) == 5
	assert find_missing_loop([4, 12, 9, 5, 6],[4, 9, 5, 6]) == 12

def test_bubble_sort():
	assert bubble_sort([1,9,5,2,6,8,3,4]) == [1, 2, 3, 4, 5, 6, 8, 9]

def test_merge_sort():
	assert merge_sort([6, 5, 3, 1, 8, 7, 2, 4, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
	assert merge_sort([1,2,-1,0,9,65,7,3,4,1,2]) == [-1,0,1,1,2,2,3,4,7,9,65]

def test_find_first_duplicate():
	assert first_duplicate([i for i in range(0,11)] + [10]) == [10]
	assert first_duplicate([i for i in range(0,6)] + [5]) == [5]
	assert first_duplicate([i for i in range(0,11)] + [3,7]) == [3,7]
	assert first_duplicate([i for i in range(0,101)] + [5,10,78]) == [5,10,78]
	assert first_duplicate([i for i in range(0,1000001)] + [1000000]) == [1000000]

def test_find_first_duplicate():
	assert sorted_squared_array([-6, -4, 1, 2, 3, 5]) == [1, 4, 9, 16, 25, 36]

def test_rotate_array():
	assert rotate_array_manually([[1,2,3],[4,5,6],[7,8,9]]) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
	assert rotate_array([[1,2,3],[4,5,6],[7,8,9]]) == [(7, 4, 1), (8, 5, 2), (9, 6, 3)]

def test_first_not_repeating():
	assert first_not_repeating('aaabccc') == 'b'
	assert first_not_repeating_table ('aaabccc') == 'b'