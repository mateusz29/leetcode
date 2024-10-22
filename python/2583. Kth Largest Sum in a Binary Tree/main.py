from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = []

        queue = deque([root])

        while queue:
            sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            sums.append(sum)

        sums.sort(reverse=True)

        return sums[k - 1] if k <= len(sums) else -1


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(8)
    root.right = TreeNode(9)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(1)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(6)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(7)
    print(s.kthLargestLevelSum(root, 2))
