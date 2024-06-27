from typing import List

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)
        charFreq = {}
        output= []

        for _ in range(len(set1)):
            num = set1.pop()
            if num not in charFreq:
                charFreq[num] = 1
            else:
                charFreq[num] += 1

        for _ in range(len(set2)):
            num = set2.pop()
            if num not in charFreq:
                charFreq[num] = 1
            else:
                charFreq[num] += 1

        for _ in range(len(set3)):
            num = set3.pop()
            if num not in charFreq:
                charFreq[num] = 1
            else:
                charFreq[num] += 1
                
        for key in charFreq.keys():
             if charFreq.get(key) > 1:
                 output.append(key)

        return output
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.twoOutOfThree([3,1], [2,3], [1,2]))