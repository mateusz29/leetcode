from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        odd_count = 0
        freq = Counter(s)
        for i in freq.values():
            if i % 2 != 0:
                odd_count += 1

        if odd_count > k:
            return False
        else:
            return True


if __name__ == "__main__":
    s = Solution()
    print(s.canConstruct("annabelle", 2))
