class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(' ')
        words_seq = ['' for _ in range(len(words))]

        for word in words:
            words_seq[int(word[-1])-1] = word[:len(word)-1]

        return " ".join(words_seq)

if __name__ == "__main__":
    solution = Solution()
    print(solution.sortSentence("is2 sentence4 This1 a3"))