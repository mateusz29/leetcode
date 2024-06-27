class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        reversed = ""
        found = False
        
        for i in range(len(word)):
            reversed += word[i]
            if word[i] == ch:
                found = True
                break
        
        if found:
            return reversed[::-1] + word[i+1:]

        return word

if __name__ == "__main__":
    solution = Solution()
    print(solution.reversePrefix("abcdefd", "d"))