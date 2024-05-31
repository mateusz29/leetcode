class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        nums = []
        for char in s:
            if char in roman:
                nums.append(roman[char])
        
        n = len(nums)
        num = 0
        for i in range(0, n - 1):
            if nums[i] < nums[i + 1]:
                num -= nums[i]
            else:
                num += nums[i]
        num += nums[n-1]
        return num

if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt("IV"))