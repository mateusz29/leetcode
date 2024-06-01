class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = s.lower()
        new_s = ""
        for char in s:
            if char in alphanumeric:
                new_s += char

        return new_s == new_s[::-1]


if __name__ == "__main__":   
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))