from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        idx = 0

        for _ in range(len(encoded)):
            first = first ^ encoded[idx]
            idx += 1
            result.append(first)

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.decode([1, 2, 3], 1))
