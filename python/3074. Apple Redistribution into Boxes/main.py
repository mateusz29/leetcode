from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        amount = sum(apple)
        capacity.sort(reverse=True)
        cnt = 0
        for box in capacity:
            amount -= box
            cnt += 1
            if amount <= 0:
                break
        
        return cnt

if __name__ == "__main__":
    s = Solution()
    print(s.minimumBoxes([5,5,5],[2,4,2,7]))