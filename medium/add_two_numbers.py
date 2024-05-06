# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rem = 0
        res = ListNode()
        res_head = res

        while head1 or head2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val_ = val1 + val2 + rem
            val = val_ % 10
            rem = 1 if val_ > 9 else 0

            res.next = ListNode(val=val)
            res = res.next
            head1 = l1.next if l1 else None
            head2 = l2.next if l2 else None
            
        if rem == 1:
            res.next = ListNode(val=1)
        return res_head.next
        