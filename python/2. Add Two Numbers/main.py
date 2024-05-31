from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head
        carry = 0

        while l1 or l2 or carry != 0:
            if l1:
                val1 = l1.val
            else:
                val1 = 0

            if l2:
                val2 = l2.val
            else:
                val2 = 0                

            sum = val1 + val2 + carry
            carry = sum // 10
            node = ListNode(sum%10)
            tail.next = node
            tail = tail.next

            if l1:
                l1 = l1.next
            else:
                l1 = None
            if l2:
                l2 = l2.next
            else:
                l2 = None

        return head.next

if __name__ == "__main__":
    print("Test")
    solution = Solution()
    print(solution.addTwoNumbers([2,4,3], [5,6,4]))