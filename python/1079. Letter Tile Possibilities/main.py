class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq = [0] * 26

        for c in tiles:
            freq[ord(c) - ord("A")] += 1

        return self._count_possibilities(freq)

    def _count_possibilities(self, freq: list) -> int:
        count = 0

        for i in range(26):
            if not freq[i]:
                continue

            count += 1
            freq[i] -= 1
            count += self._count_possibilities(freq)
            freq[i] += 1

        return count


if __name__ == "__main__":
    s = Solution()
    print(s.numTilePossibilities("AAB"))
