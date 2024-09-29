from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []

        def inorder_traversal(root: Optional[TreeNode]):
            if root is None:
                return

            inorder_traversal(root.left)
            result.append(root.val)
            inorder_traversal(root.right)

        inorder_traversal(root)
        return result[k - 1]
