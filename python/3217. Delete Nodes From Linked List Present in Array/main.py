from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(
        self, nums: list[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        nums = set(nums)

        while head and head.val in nums:
            head = head.next

        current = head
        while current.next:
            if current.next.val in nums:
                current.next = current.next.next
            else:
                current = current.next

        return head


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head = s.modifiedList([1, 2, 3], head)
    for i in range(5):
        print(head.val)
        head = head.next
