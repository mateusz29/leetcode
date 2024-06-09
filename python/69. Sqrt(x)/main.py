class Solution:
    def mySqrt(self, x: int) -> int:
        if not x:
            return x
        left, right = 1, x

        while left <= right:
            mid = (left + right) // 2
            if x // mid == mid:
                return mid 
            elif x // mid < mid:
                right = mid - 1
            else:
                left = mid + 1

        return right

if __name__ == "__main__":
    solution = Solution()
    print(solution.mySqrt(8))