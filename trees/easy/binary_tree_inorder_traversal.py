from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        roots = []
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            roots.append(root.val)
            traverse(root.right)
        traverse(root)
        return roots
    
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root:
            result += self.inorderTraversal(root.left)
            result.append(root.val)
            result += self.inorderTraversal(root.right)
        
        return result
    
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        stack = []
        roots = []
        while True:
            if curr:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                roots.append(curr.val)
                curr = curr.right
            else:
                break

        return roots


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result, stack = [], []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return result

            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result

        