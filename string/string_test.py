from reverse import reverse_while, reverse_slicing, reverse_using_loop
from first_recurring import first_recurring

def test_reverse():
	for (string_, check) in [('abc','cba'), ('def','fed'),('ghi','ihg'),('jkl','lkj'),('mno','onm'),('pqr','rqp'),('stu','uts')]:
		assert reverse_while(string_) == check
		assert reverse_slicing(string_) == check
		assert reverse_using_loop(string_) == check


def test_first_recurring():
	assert first_recurring('DBCABA') == 'B'