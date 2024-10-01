from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []

        def inorder_traversal(root: Optional[TreeNode]) -> None:
            if root is None:
                return

            inorder_traversal(root.left)
            values.append(root.val)
            inorder_traversal(root.right)

        inorder_traversal(root)

        for i in range(1, len(values)):
            if values[i - 1] >= values[i]:
                return False

        return True
