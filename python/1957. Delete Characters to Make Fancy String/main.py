class Solution:
    def makeFancyString(self, s: str) -> str:
        fancy = []
        prev = ""
        count = 1
        for c in s:
            if c == prev:
                count += 1
            else:
                count = 1
            if count < 3:
                fancy.append(c)
            prev = c
        return "".join(fancy)


if __name__ == "__main__":
    s = Solution()
    print(s.makeFancyString("leeetcode"))