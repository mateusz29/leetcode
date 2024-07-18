class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        for i, word in enumerate(words):
            if word[0].lower() in "aeiou":
                words[i] = word + "ma" + "a" * (i + 1)
            else:
                words[i] = word[1:] + word[0] + "ma" + "a" * (i + 1)
        return " ".join(words)

if __name__ == "__main__":
    s = Solution()
    print(s.toGoatLatin("I speak Goat Latin"))