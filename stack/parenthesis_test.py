from parenthesis import check_bracket
def test_checking():
	assert check_bracket('(()') == 2
	assert check_bracket(')()())') == 4
	assert check_bracket(')()())') ==  4
	assert check_bracket(')()())))') == 4
	assert check_bracket('(((())))))))))))))))))') == 8