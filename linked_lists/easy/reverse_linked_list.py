from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        rev = None
        node = None
        while head:
            node = ListNode(val=head.val)
            node.next = rev   
            rev = node         
            head = head.next

        return node

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current, prev = head, None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
            