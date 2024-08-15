class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        words_rev = [word[::-1] for word in words]
        return ' '.join(words_rev)

if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("Let's take LeetCode contest"))