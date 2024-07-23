class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = [0 for _ in range(26)]
        for char in s:
            counts[ord(char) - 97] += 1
        
        for i, char in enumerate(s):
            if counts[ord(char) - 97] == 1:
                return i
        
        return -1

if __name__ == "__main__":
    s = Solution()
    print(s.firstUniqChar("leetcode"))