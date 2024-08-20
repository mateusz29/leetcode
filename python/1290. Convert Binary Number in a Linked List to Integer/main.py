# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bits = []
        while head:
            bits.append(str(head.val))
            head = head.next

        return int("".join(bits), 2)


if __name__ == "__main__":
    s = Solution()
    print(s.getDecimalValue([1, 0, 1]))
