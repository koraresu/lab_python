from find_missing_number import missing_number_in_array

def test_missing_number_in_array():
	assert missing_number_in_array([1,2,3,4,6],6) == 5
	assert missing_number_in_array([1, 2, 3, 4, 6, 7, 9, 8, 10],10) == 5
	assert missing_number_in_array([1, 2, 3, 4, 6, 5, 7, 9, 10],10) == 8
	assert missing_number_in_array([1, 10, 2, 6, 7, 4, 9, 5, 8],10) == 3