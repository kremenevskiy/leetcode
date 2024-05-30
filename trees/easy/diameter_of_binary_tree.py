from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mx_diam = 0
        def get_height(root):
            nonlocal mx_diam
            if not root:
                return 0
            right_height = get_height(root.right)
            left_height = get_height(root.left)

            mx_diam = max(left_height + right_height, mx_diam)
            return max(right_height, left_height) + 1
        get_height(root)
        return mx_diam
