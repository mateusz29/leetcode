class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        minutes = []

        for time in timePoints:
            h, m = time.split(":")
            minutes.append(int(h) * 60 + int(m))

        minutes.sort()

        min_diff = 2000

        for i in range(len(minutes) - 1):
            min_diff = min(minutes[i + 1] - minutes[i], min_diff)

        min_diff = min(24 * 60 - minutes[-1] + minutes[0], min_diff)

        return min_diff


if __name__ == "__main__":
    s = Solution()
    print(s.findMinDifference(["01:01", "02:01", "03:00", "01:30"]))
