from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for operation in operations:
            if operation == 'C':
                record.pop()
            elif operation == 'D':
                record.append(record[-1] << 1)
            elif operation == '+':
                record.append(record[-1] + record[-2])
            else:
                record.append(int(operation))
        return sum(record)

if __name__ == "__main__":
    s = Solution()
    print(s.calPoints(["5","2","C","D","+"]))