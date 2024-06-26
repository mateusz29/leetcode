class Solution:
    def sumBase(self, n: int, k: int) -> int:
        new = ""
        while n != 0:
            rest = n % k
            n = (n - rest) / k
            new += str(int(rest))
        
        num_sum = 0
        new_num = int(new[::-1])

        while new_num != 0:
            rest = new_num % 10
            new_num = (new_num - rest) / 10
            num_sum += rest
        return int(num_sum)

if __name__ == "__main__":
    solution = Solution()
    print(solution.sumBase(34, 6))