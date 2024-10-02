class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        result = []
        arr_sorted = sorted(list(set(arr)))
        
        rankings = {}
        for rank, num in enumerate(arr_sorted):
            rankings[num] = rank + 1

        for num in arr:
           result.append(rankings[num])
        
        return result        


if __name__ == "__main__":
    s = Solution()
    print(s.arrayRankTransform([100, 100, 100]))
