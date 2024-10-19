class Solution:    
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s: str) -> str:
            inverted_bits = []
            for c in s:
                if c == "0":
                    inverted_bits.append("1")
                else:
                    inverted_bits.append("0")
            return "".join(inverted_bits)
        
        result = "0"
        for _ in range(1, n):
            result = result + "1" + invert(result)[::-1]

        return result[k - 1]


if __name__ == "__main__":
    s = Solution()
    print(s.findKthBit(4, 11))