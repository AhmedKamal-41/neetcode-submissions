class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        if len(s) != len(t):
            return False

        found = {}

        # Count each character in s.
        for i in range(len(s)):
            found[s[i]] = found.get(s[i], 0) + 1

        # Use up those counts with the characters in t.
        for i in range(len(t)):
            if t[i] not in found:
                return False

            found[t[i]] -= 1

            if found[t[i]] == 0:
                del found[t[i]]

        return not found