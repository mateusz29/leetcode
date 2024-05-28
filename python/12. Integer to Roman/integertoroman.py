class Solution:
    def intToRoman(self, num: int) -> str:
        roman_num = ""
        thousands = num // 1000
        roman_num += 'M'*thousands

        hundreds = (num % 1000) // 100
        if hundreds == 9:
            roman_num += "CM"
        elif hundreds == 4:
            roman_num += "CD"
        elif hundreds == 5:
            roman_num += "D"
        elif hundreds > 5:
            roman_num += "D" + (hundreds - 5) * "C"
        else:
            roman_num += "C" * hundreds

        tens = (num % 100) // 10
        if tens == 9:
            roman_num += "XC"
        elif tens == 4:
            roman_num += "XL"
        elif tens == 5:
            roman_num += "L"
        elif tens > 5:
            roman_num += "L" + (tens - 5) * "X"
        else:
            roman_num += "X" * tens

        ones = (num % 10)
        if ones == 9:
            roman_num += "IX"
        elif ones == 4:
            roman_num += "IV"
        elif ones == 5:
            roman_num += "V"
        elif ones > 5:
            roman_num += "V" + (ones - 5) * "I"
        else:
            roman_num += "I" * ones
            
        return roman_num


if __name__ == "__main__":
    solution = Solution()
    print(solution.intToRoman(58))