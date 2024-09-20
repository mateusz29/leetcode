class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        result = [[]]

        for num in nums:
            found = False
            for i in range(len(result)):
                if num not in result[i]:
                    found = True
                    result[i].append(num)
                    break
            if not found:
                result.append([num])
        
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.findMatrix([1,2,3,4]))