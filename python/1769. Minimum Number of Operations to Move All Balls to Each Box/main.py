class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        n = len(boxes)
        result = []

        for i in range(n):
            cnt = 0
            for j, num in enumerate(boxes):
                if num == "1":
                    cnt += abs(i - j)
            result.append(cnt)

        return result
    

if __name__ == "__main__":
    s = Solution()
    print(s.minOperations("001011"))