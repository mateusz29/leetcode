from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.found = set()
        self.repair(root, 0)

    def find(self, target: int) -> bool:
        return target in self.found

    def repair(self, node: Optional[TreeNode], value: int):
        if node is None:
            return
        self.found.add(value)
        self.repair(node.left, 2 * value + 1)
        self.repair(node.right, 2 * value + 2)


# Your FindElements object will be instantiated and called as such:
root = TreeNode(-1, None, TreeNode(-1, None, None))
obj = FindElements(root)
print(obj.find(1))
print(obj.find(2))
