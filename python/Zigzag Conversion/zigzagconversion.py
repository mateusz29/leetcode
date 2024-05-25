class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        array = [[] for _ in range(numRows)]

        i = 0
        a = 1
        for char in s:
            array[i].append(char)
            if i == 0:
                a = 1
            elif i == numRows-1:
                a = -1
            i += a
            
        string = ""
        for i in range(numRows):
            for char in array[i]:
                string += char

        return string

if __name__ == "__main__":
    solution = Solution()
    print(solution.convert("PAYPALISHIRING", 4))