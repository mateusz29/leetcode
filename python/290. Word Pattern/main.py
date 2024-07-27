class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        found = {}
        for i, chr in enumerate(pattern):
            if chr not in found.keys():
                if words[i] in found.values():
                    return False
                found[chr] = words[i]
            else:
                if words[i] != found[chr]:
                    return False
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.wordPattern("abba", "dog dog dog dog"))