class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split_words = s.split(' ')
        words = []
        for word in split_words:
            if word != '':
                words.append(word)
        return len(words[len(words)-1])

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLastWord("   fly me   to   the moon  "))