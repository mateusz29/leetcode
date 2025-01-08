class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        def isPrefixAndSuffix(str1: str, str2: str) -> bool:
            return str2.startswith(str1) and str2.endswith(str1)

        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if len(words[i]) > len(words[j]):
                    continue

                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1

        return count


if __name__ == "__main__":
    s = Solution()
    print(s.countPrefixSuffixPairs(["a", "aba", "ababa", "aa"]))
