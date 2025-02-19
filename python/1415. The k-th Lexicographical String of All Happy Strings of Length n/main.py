class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        current = ""
        happy_strings = []

        self._happy_strings(n, current, happy_strings)

        if len(happy_strings) < k:
            return ""
        else:
            return happy_strings[k - 1]
    
    def _happy_strings(self, n: int, current: str, happy_strings: list):
        if len(current) == n:
            happy_strings.append(current)
            return
        
        for c in ['a', 'b', 'c']:
            if len(current) > 0 and current[-1] == c:
                continue
            self._happy_strings(n, current + c, happy_strings)

if __name__ == "__main__":
    s = Solution()
    print(s.getHappyString(3, 9))