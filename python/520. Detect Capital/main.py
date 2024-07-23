class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower() or word.istitle():
            return True
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.detectCapitalUse("USA"))