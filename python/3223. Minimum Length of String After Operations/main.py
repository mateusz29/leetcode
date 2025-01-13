class Solution:
    def minimumLength(self, s: str) -> int:
        freq = [0] * 26
        ans = 0

        for c in s:
            freq[ord(c) - ord("a")] += 1

        for f in freq:
            if f == 0:
                continue
            if f % 2 == 0:
                ans += 2
            else:
                ans += 1

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.minimumLength("abaacbcbb"))
