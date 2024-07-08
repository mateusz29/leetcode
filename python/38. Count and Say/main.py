class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        string = self.countAndSay(n - 1)
        out = ""
        cnt = 1
        for i in range(len(string)):
            if i+1 < len(string) and string[i] == string[i+1]:
                cnt += 1
            else:
                out += str(cnt)
                out += string[i]
                cnt = 1
        return out

if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(4))