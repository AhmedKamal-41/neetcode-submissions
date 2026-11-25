class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #edge case
        if len(s) != len(t):
            return False
        
        sorted_s, sorted_t = sorted(s), sorted(t)

        for i in range(len(t)):
            if sorted_s[i] != sorted_t[i]:
                return False
        return True   