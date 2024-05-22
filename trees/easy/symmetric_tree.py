from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        res = True
        def check(left, right):
            if left and right:        
                if left.val == right.val:    
                    check(left.left, right.right)
                    check(left.right, right.left) 
            elif left is None and right is None:
                return
            else:
                res = False
        check(root.left, root.right)
        return res
    

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def same(left, right):
            if not left and not right:
                return 1
            if not left or not right:
                return 0
            if left.val == right.val and same(left.left, right.rigth) and same(left.right, right.left):
                return 1
            return 0
        return same(root.left, root.right)
    

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = [root.left, root.right]
        
        while stack:
            left, right = stack.pop(), stack.pop()
            if left is None and right is None:
                continue
            elif not left or not right:
                return False
            elif left.val == right.val:
                stack += [left.left, right.right, left.right, right.left]
            else:
                return False
        return True