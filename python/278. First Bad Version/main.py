# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    ...

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        num = 0
        while start <= end:
            mid = start + (end - start) // 2
            if isBadVersion(mid):
                num = mid
                end = mid - 1
            else:
                start = mid + 1
        return num

if __name__ == "__main__":
    solution = Solution()
    print(solution.firstBadVersion(5))