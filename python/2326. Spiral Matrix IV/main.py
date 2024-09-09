from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> list[list[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        tmp_matrix = [[-1 for _ in range(n)] for _ in range(m)]
        x_p, y_p, x, y = 1, 0, 0, 0

        while head:
            matrix[y][x] = head.val
            tmp_matrix[y][x] = 0
            head = head.next
            if not 0 <= x + x_p < n or not 0 <= y + y_p < m or tmp_matrix[y+y_p][x+x_p] == 0:
                x_p, y_p = -y_p, x_p

            x += x_p
            y += y_p

        return matrix


if __name__ == "__main__":
    s = Solution()
    print(s.spiralMatrix(3, 5, ListNode(3, ListNode(0, ListNode(2, ListNode(6, ListNode(8, ListNode(1, ListNode(7, ListNode(9, ListNode(4, ListNode(2, ListNode(5, ListNode(5, ListNode(0)))))))))))))))