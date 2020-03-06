from linked_list import ListNode, Solution
def test_linked_list():
	l1_3 = ListNode(3)
	l1_2 = ListNode(4)
	l1_2.next = l1_3
	l1   = ListNode(2)
	l1.next = l1_2
	l2_3 = ListNode(4)
	l2_2 = ListNode(6)
	l2_2.next = l2_3
	l2   = ListNode(5)
	l2.next = l2_2

	a = Solution()
	x = a.add_two_numbers(l1, l2)
	assert x.val == 7
	assert x.next.val == 0
	assert x.next.next.val == 8

