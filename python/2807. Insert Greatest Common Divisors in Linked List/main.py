from typing import Optional 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head

        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a
        
        current = head
        while current.next:
            val_between = gcd(current.val, current.next.val)
            current.next = ListNode(val_between, current.next)
            current = current.next.next
        
        return head

if __name__ == "__main__":
    s = Solution()
    print(s.insertGreatestCommonDivisors(ListNode(18, ListNode(6, ListNode(10, ListNode(3))))))