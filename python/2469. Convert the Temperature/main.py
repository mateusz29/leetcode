from typing import List

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans = []
        ans.append(celsius + 273.15)
        ans.append(celsius * 1.8 + 32)

        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.convertTemperature(36.50))