from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dum = ListNode(next=head)
        dum1 = dum2 = dum

        for _ in range(n + 1):
            dum1 = dum1.next

        while dum1:
            dum2 = dum2.next
            dum1 = dum1.next
        
        dum2.next = dum2.next.next

        return dum.next