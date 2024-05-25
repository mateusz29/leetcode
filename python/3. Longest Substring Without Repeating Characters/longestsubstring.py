class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        leng = 0 
        maxlen = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] not in substring:
                    substring += s[j]
                    leng += 1
                    if (leng > maxlen):
                        maxlen = leng
                else:
                    substring = ""
                    leng = 0
                    break
        return maxlen

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("jbpnbwwd"))