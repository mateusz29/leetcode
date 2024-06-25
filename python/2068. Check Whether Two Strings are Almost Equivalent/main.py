class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        def charFreq(word: str) -> dict:
            wordFreq = {}
            for char in word:
                if char not in wordFreq:
                    wordFreq[char] = 1
                else:
                    wordFreq[char] += 1
            return wordFreq

        word1Freq = charFreq(word1)
        word2Freq = charFreq(word2)
        allChars = word1Freq.keys() | word2Freq.keys()

        for char in allChars:
            if abs(word1Freq.get(char, 0) - word2Freq.get(char, 0)) > 3:
                return False
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.checkAlmostEquivalent("aaaa", "baccb"))