import math
import heapq

class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        score = 0
        heap = [-num for num in nums]
        heapq.heapify(heap)
        
        for _ in range(k):
            max_val = -heapq.heappop(heap)
            score += max_val
            heapq.heappush(heap, -math.ceil(max_val / 3))
            
        return score

if __name__ == "__main__":
    s = Solution()
    print(s.maxKelements([10, 10, 10, 10, 10], 5))