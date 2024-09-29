from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = []
        def preorder_traversal(root: Optional[TreeNode], num: str):
            if root is None:
                return

            num += str(root.val)
            if root.left is None and root.right is None:
                result.append(int(num))

            preorder_traversal(root.left, num)
            preorder_traversal(root.right, num)

        preorder_traversal(root, "")
        return sum(result)
