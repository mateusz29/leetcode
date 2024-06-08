from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        if root.left is None and root.right is None:
            return root.val == targetSum
        
        leftSum = self.hasPathSum(root.left, targetSum - root.val)
        rightSum = self.hasPathSum(root.right, targetSum - root.val)

        return leftSum or rightSum

if __name__ == "__main__":
    solution = Solution()