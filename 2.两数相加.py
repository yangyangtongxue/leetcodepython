# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		carry = 0
		res = ListNode(0)
		r = res
		while (l1 or l2):
			x = l1.val if l1 else 0
			y = l2.val if l2 else 0
			s = x+y+carry
			carry = (s//10)
			r.next = ListNode(s%10)
			r = r.next
			if l1:
				l1 = l1.next
			if l2：
				l2 = l2.next
		if carry:
			r.next = ListNode(carry)
		return res.next
			