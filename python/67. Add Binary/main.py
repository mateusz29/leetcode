class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lena = len(a) - 1
        lenb = len(b) - 1
        carry = 0
        added = ""

        while lena >= 0 or lenb >=0 or carry:
            if lena >= 0:
                carry += int(a[lena])
                lena -= 1
            if lenb >= 0:
                carry += int(b[lenb])
                lenb -= 1
            added += str(carry % 2)
            carry = carry // 2

        return added[::-1]

if __name__ == "__main__":
    solution = Solution()
    print(solution.addBinary("1010","1011"))