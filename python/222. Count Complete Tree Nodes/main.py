from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        cnt = 0
        if root:
            cnt += 1
            cnt += self.countNodes(root.left)
            cnt += self.countNodes(root.right)
        return cnt
