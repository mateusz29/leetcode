class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_list,t_list = list(s), list(t)
        s_list.sort()
        t_list.sort()
        
        for i in range(len(s_list)):
            if s_list[i] != t_list[i]:
                return False
        return True

if __name__ == "__main__":   
    solution = Solution()
    print(solution.isAnagram("a","ab"))