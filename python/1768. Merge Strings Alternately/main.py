class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        word_length = len(word1) + len(word2)
        i = 0
        w1, w2 = 0, 0
        while len(output) != word_length:
            if i % 2 == 0 and w1 < len(word1):
                output += word1[w1]
                w1 += 1
            elif w2 < len(word2):
                output += word2[w2]
                w2 += 1
            i += 1
        return output

if __name__ == "__main__":
    s = Solution()
    print(s.mergeAlternately("ab", "pqrs"))