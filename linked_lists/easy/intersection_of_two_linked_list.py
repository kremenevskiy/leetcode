from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        first, second = headA, headB

        while first != second:
            first = first.next if first else headB
            second = second.next if second else headA

        return first


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        m = set()
        while headA:
            print(headA.val)
            m.add(headA)
            headA = headA.next
        while headB:
            if headB in m:
                return headB
            headB = headB.next
        return None