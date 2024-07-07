from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiopQWERTYUIOP"
        row2 = "asdfghjklASDFGHJKL"
        row3 = "zxcvbnmZXCVBNM"
        can_typed = []

        for word in words:
            b1 = b2 = b3 = True
            for letter in word:
                if letter not in row1:
                    b1 = False
                if letter not in row2:
                    b2 = False
                if letter not in row3:
                    b3 = False
            if b1 or b2 or b3:
                can_typed.append(word)
        
        return can_typed

if __name__ == "__main__":
    s = Solution()
    print(s.findWords(["Hello","Alaska","Dad","Peace"]))