from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        if len(arr) == 1:
            return True
        
        freqs = {}
        for num in arr:
            freqs[num] = freqs.get(num, 0) + 1

        return len(freqs) == len(set(freqs.values()))
        

if __name__ == "__main__":
    s = Solution()
    print(s.uniqueOccurrences([1,2,2,1,1,3]))