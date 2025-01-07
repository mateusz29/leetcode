class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        ans = []
        for word in words:
            for word1 in words:
                if word in word1 and word != word1 and word not in ans:
                    ans.append(word)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.stringMatching(["mass","as","hero","superhero"]))