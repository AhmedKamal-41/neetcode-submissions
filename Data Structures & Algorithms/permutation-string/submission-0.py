class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        hashmap = {}
        need = {}

        for char in s1:
            hashmap[char] = hashmap.get(char, 0) + 1

        for r in range(len(s2)):
            need[s2[r]] = need.get(s2[r], 0) + 1

            if (r- l + 1) > len(s1):
                need[s2[l]] -= 1

                if need[s2[l]] == 0:
                    del need[s2[l]]
                l+=1

            if need == hashmap:
                return True
        return False




        
