class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        complement = []
        for char in binary:
            if char == '0':
                complement.append('1')
            else:
                complement.append('0')
        
        return int(''.join(complement), 2)

if __name__ == "__main__":
    s =Solution()
    print(s.findComplement(31287))