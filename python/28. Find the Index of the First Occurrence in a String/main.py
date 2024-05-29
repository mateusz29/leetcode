class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        cnt = 0
        for i in range(len(haystack) - len(needle)+1):
            for j in range(len(needle)):
                if haystack[i+j] == needle[j]:
                    cnt += 1
            if cnt == len(needle):
                return i
            cnt = 0
        return -1
        #return (haystack.find(needle))

if __name__ == "__main__":
    solution = Solution()
    print(solution.strStr("a","a"))