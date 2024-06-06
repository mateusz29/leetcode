from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        for num in nums:
            if num == val:
                counter += 1
        print(counter)
        for _ in range(counter):
            nums.remove(val)
        return len(nums)

if __name__ == "__main__":
    solution = Solution()
    test = [0,1,2,2,3,0,4,2]
    print(solution.removeElement(test,2))
    print(test)