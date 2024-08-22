class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        found = []
        for c in s:
            if c in vowels:
                found.append(c)

        found.sort()
        result = []
        j = 0
        for i in range(len(s)):
            if s[i] in vowels:
                result.append(found[j])
                j += 1
            else:
                result.append(s[i])

        return "".join(result)


if __name__ == "__main__":
    s = Solution()
    print(s.sortVowels("lEetcOde"))
