class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()

        target = skill[0] + skill[len(skill) - 1]
        product = skill[0] * skill[len(skill) - 1]
    
        size = len(skill)
        for i in range(1, size//2):
            if skill[i] + skill[size - i - 1] == target:
                product += skill[i] * skill[size - i - 1]
            else:
                return -1
        
        return product        


if __name__ == "__main__":
    s = Solution()
    print(s.dividePlayers([3, 4]))
