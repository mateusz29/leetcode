class Solution:
    def check(self, s: str) -> bool:
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        palindrome = ""
        long_palindrome = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                palindrome += s[j]
                if self.check(palindrome):
                    if len(palindrome) > len(long_palindrome):
                        long_palindrome = palindrome
            palindrome = ""
        return long_palindrome

if __name__ == "__main__":   
    solution = Solution()
    print(solution.longestPalindrome("babad"))