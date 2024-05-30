from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reversed_list = None
        new_head = head
        while new_head:
            new_node = ListNode(val=new_head.val)
            new_node.next = reversed_list
            reversed_list = new_node
            new_head = new_head.next
        
        while head or reversed_list:
            if head.val == reversed_list.val:
                head = head.next
                reversed_list = reversed_list.next
            else:
                return False
        return head is None and reversed_list is None


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_len = 0
        h = head
        while h:
            list_len += 1
            h = h.next
        
        if list_len % 2 == 0:
            mid = list_len // 2
        else:
            mid = list_len // 2 + 1
        
        mid_list = head
        rev = None
        for i in range(mid):
            next_node = mid_list.next
            mid_list.next = rev
            rev = mid_list

            mid_list = next_node
        
        if list_len % 2 == 1:
            rev = rev.next
        
        while mid_list:
            if mid_list.val == rev.val:
                mid_list, rev = mid_list.next, rev.next
            else:
                return False
        return True


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return nums == nums[::-1]


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reversed_node = None
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            reversed_node, reversed_node.next, slow = slow, reversed_node, slow.next
        
        if fast:
            slow = slow.next
        
        while slow:
            if slow.val != reversed_node.val:
                return False
            slow, reversed_node = slow.next, reversed_node.next
        return True
    

