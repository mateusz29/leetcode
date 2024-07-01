class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        used = {}
        for i in range(len(s)):
            if s[i] not in used:
                if t[i] in used.values():
                    return False
                used[s[i]] = t[i]
            else:
                if t[i] != used[s[i]]:
                    return False
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isIsomorphic("egg", "add"))