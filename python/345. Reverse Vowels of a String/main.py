class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        found = []
        output = ""

        for char in s:
            if char in vowels:
                found.append(char)

        for char in s:
            if char in vowels:
                output += found.pop()
            else:
                output += char

        return output

if __name__ == "__main__":
    s = Solution()
    print(s.reverseVowels("aAsaohjdasBVA"))