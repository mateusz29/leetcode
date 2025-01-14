class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        freqA, freqB = {}, {}
        ans = []
        common_count = 0

        for i, num in enumerate(A):
            freqA[num] = freqA.get(num, 0) + 1
            freqB[B[i]] = freqB.get(B[i], 0) + 1

            if num in freqB:
                common_count += 1
            if B[i] in freqA and B[i] != num:
                common_count += 1

            ans.append(common_count)

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.findThePrefixCommonArray([1, 3, 2, 4], [3, 1, 2, 4]))
