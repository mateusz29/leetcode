from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            row.reverse()
        
        for row in image:
            for i in range(len(row)):
                row[i] = int(not row[i])

        return image

if __name__ == "__main__":
    s = Solution()
    print(s.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))