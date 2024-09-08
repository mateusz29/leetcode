from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> list[Optional[ListNode]]:
        length = 0
        current = head

        while current:
            length += 1
            current = current.next

        n, r = divmod(length, k)
        reuslt = []
        for i in range(k):
            part = head
            for _ in range(n + (i < r) - 1):
                if head:
                    head = head.next
            if head:
                head.next, head = None, head.next
            reuslt.append(part)

        return reuslt


if __name__ == "__main__":
    s = Solution()
    s.splitListToParts(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10)))))))))), 3)