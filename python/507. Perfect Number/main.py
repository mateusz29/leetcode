class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisors = []        
        for i in range(1,int(num**0.5)+1):
            if num%i == 0:
                divisors.append(i)
                if i != num//i:
                    divisors.append(num//i)
        return sum(divisors) == 2*num
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.checkPerfectNumber(1))