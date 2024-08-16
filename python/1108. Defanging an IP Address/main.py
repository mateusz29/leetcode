class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged = []
        for char in address:
            if char == '.':
                defanged.append('[.]')
            else:
                defanged.append(char)
        
        return ''.join(defanged)

if __name__ == '__main__':
    s = Solution()
    print(s.defangIPaddr("1.1.1.1"))