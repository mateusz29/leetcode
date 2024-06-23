class Solution:
    def maxPower(self, s: str) -> int:
        s += '#'
        count = 1
        counts = [0 for _ in range(26)]
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count += 1
            else:
                idx = ord(s[i]) - 97
                if counts[idx] < count:
                    counts[idx] = count
                count = 1
        return max(counts)
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxPower("abbcccddddeeeeedcbaa"))