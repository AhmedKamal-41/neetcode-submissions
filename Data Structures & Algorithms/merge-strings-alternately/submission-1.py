class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_str = ""
        l = 0
        r = 0
        
        while l < len(word1) and r < len(word2):
            new_str+=word1[l]
            l+=1
            new_str+=word2[r]
            r+=1
        new_str +=word1[l:]
        new_str+= word2[r:]

        return new_str
        