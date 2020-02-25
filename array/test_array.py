from find_missing_number import missing_number_in_array
from find_missing_element import find_missing_set, find_missing_loop
from sort_problem import bubble_sort
from find_first_duplicate import first_duplicate
from sorted_squared_array import sorted_squared_array

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

def test_find_first_duplicate():
	assert first_duplicate([i for i in range(0,11)] + [10]) == [10]
	assert first_duplicate([i for i in range(0,6)] + [5]) == [5]
	assert first_duplicate([i for i in range(0,11)] + [3,7]) == [3,7]
	assert first_duplicate([i for i in range(0,101)] + [5,10,78]) == [5,10,78]
	assert first_duplicate([i for i in range(0,1000001)] + [1000000]) == [1000000]

def test_find_first_duplicate():
	assert sorted_squared_array([-6, -4, 1, 2, 3, 5]) == [1, 4, 9, 16, 25, 36]
