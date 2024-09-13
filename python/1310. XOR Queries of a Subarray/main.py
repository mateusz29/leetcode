class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        result = []
        n = len(arr)
        pre = [0] * n
        pre[0] = arr[0]

        for i in range(1, n):
            pre[i] = pre[i - 1] ^ arr[i]

        for left, right in queries:
            if left == 0:
                result.append(pre[right])
            else:
                result.append(pre[right] ^ pre[left - 1])

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.xorQueries([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]]))
