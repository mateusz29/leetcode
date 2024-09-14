class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_num = max(nums)
        longest = 0
        cnt = 0

        for num in nums:
            if num == max_num:
                cnt += 1
                longest = max(longest, cnt)                
            else:
                cnt = 0
                
        return longest

if __name__ == "__main__":
    s = Solution()
    print(s.longestSubarray([311155,311155,311155,311155,311155,311155,311155,311155,201191,311155]))