from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.

        """
        if not root:
            return
        
        dummy = TreeNode()
        current = dummy

        def preorder_traversal(node: Optional[TreeNode]) -> None:
            nonlocal current
            if node is None:
                return

            current.right = node
            current.left = None
            current = current.right
            right_subtree = node.right

            preorder_traversal(node.left)
            preorder_traversal(right_subtree)

        preorder_traversal(root)

        return dummy.right
        