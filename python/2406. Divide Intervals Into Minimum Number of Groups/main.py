class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        lefts = sorted([x[0] for x in intervals])
        rights = sorted([x[1] for x in intervals])
        result, right_ptr = 0, 0

        for left in lefts:
            if left > rights[right_ptr]:
                right_ptr += 1
            else:
                result += 1

        return result 


if __name__ == "__main__":
    s = Solution()
    print(s.minGroups([[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]))
