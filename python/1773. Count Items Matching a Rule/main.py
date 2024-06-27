from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        
        if ruleKey == "type":
            idx = 0
        elif ruleKey == "color":
            idx = 1
        elif ruleKey == "name":
            idx = 2
        
        for item in items:
            if item[idx] == ruleValue:
                count += 1
        
        return count

if __name__ == "__main__":
    solution = Solution()
    print(solution.countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver"))