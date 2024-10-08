class Solution:
    def minSwaps(self, s: str) -> int:
        result = 0
        
        for bracket in s:
            if bracket == "[":
                result += 1
            elif bracket == "]" and result > 0:
                result -= 1

        return (result + 1) // 2


if __name__ == "__main__":
    s = Solution()
    print(s.minSwaps("][]["))