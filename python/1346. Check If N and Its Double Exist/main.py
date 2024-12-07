class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        x = set()

        for num in arr:
            if num * 2 in x or num / 2 in x:
                return True
            x.add(num)

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.checkIfExist([10, 2, 5, 3]))
