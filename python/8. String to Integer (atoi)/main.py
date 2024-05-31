class Solution:
    def myAtoi(self, s: str) -> int:
        a = 1
        s_read = True
        leading = True
        output = ""
        for char in s:
            if char == ' ' and leading:
                continue
            elif char == '-' and s_read:
                a = -1
                leading = False
                s_read = False
            elif char == '+' and s_read:
                a = 1
                leading = False
                s_read = False 
            elif not char.isdigit():
                leading = False
                break
            else:
                leading = False
                output += char
                s_read = False

        if output == '':
            return 0
        num = int(output) * a

        if num < -pow(2,31):
            return -pow(2,31)
        elif num > pow(2,31)-1:
            return pow(2,31)-1 
        else:
            return num

if __name__ == "__main__":
    solution = Solution()

    print(solution.myAtoi("   +0 123"))