from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    from collections import deque

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def bfs(root):
            queue = deque()
            if root:
                queue.append(root)
            level = 0
            while len(queue) > 0:
                level+=1
                for i in range(len(queue)):
                    curr = queue.popleft()
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
            return level
        return bfs(root)
    

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1