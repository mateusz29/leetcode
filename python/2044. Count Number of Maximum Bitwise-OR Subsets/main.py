class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num
        
        n = len(nums)
        def backtrack(index, current_or):
            if index == n:
                return 1 if current_or == max_or else 0
            
            return backtrack(index + 1, current_or) + backtrack(index + 1, current_or | nums[index])
        
        return backtrack(0, 0)
        

if __name__ == "__main__":
    s = Solution()
    print(s.countMaxOrSubsets([3, 1]))