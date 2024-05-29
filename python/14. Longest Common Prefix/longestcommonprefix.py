from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        strs.sort(key=len)
        n = len(strs)
        j, cnt = 0, 0
        for char in strs[0]:
            for i in range(1, n):
                if strs[i][j] == char:
                    cnt += 1
            if cnt == n - 1:
                prefix += char
            else:
                break
            j += 1
            cnt = 0
        return prefix

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["dog","racecar","car"]))