class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        vowels = {"a", "e", "i", "o", "u"}
        ans = [0] * len(queries)
        vowel_strings_sums = [0] * len(words)
        sum = 0

        for i, word in enumerate(words):
            if word[0] in vowels and word[len(word) - 1] in vowels:
                sum += 1
            vowel_strings_sums[i] = sum

        for i, query in enumerate(queries):
            if query[0] == 0:
                ans[i] = vowel_strings_sums[query[1]]
            else:
                ans[i] = vowel_strings_sums[query[1]] - vowel_strings_sums[query[0] - 1]

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.vowelStrings(["aba", "bcb", "ece", "aa", "e"], [[0, 2], [1, 4], [1, 1]]))
