from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsFreq = {}
        for char in chars:
            if char not in charsFreq:
                charsFreq[char] = 1
            else:
                charsFreq[char] += 1
        
        result = 0
        for word in words:
            wordFreq = {}
            for char in word:
                if char not in wordFreq:
                    wordFreq[char] = 1
                else:
                    wordFreq[char] += 1

            canBeFormed = True
            for char, count in wordFreq.items():
                if char not in charsFreq or charsFreq[char] < count:
                    canBeFormed = False
                    break

            if canBeFormed:
                result += len(word)

        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.countCharacters(["cat","bt","hat","tree"],"atach"))