from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def create_subtrees(left, right):
            if left > right:
                return None
            m = (left + right) // 2
            root = TreeNode(val=nums[m])
            root.left = create_subtrees(left, m-1)
            root.right = create_subtrees(m + 1, right)
            return root
        return create_subtrees(0, len(nums)-1)

nums = [-10,-3,0,5,9]
Solution().sortedArrayToBST(nums)

