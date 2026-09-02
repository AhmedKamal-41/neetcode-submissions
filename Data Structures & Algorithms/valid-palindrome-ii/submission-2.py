class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skipl = s[l+1:r+1] # add everything in the array except the l itself
                skipr= s[l:r] # add everything in the array except the r itself

                return (skipl == skipl[::-1]) or (skipr == skipr[::-1]) # no two pointer now: just the regular Palindrome problem
            l += 1
            r -= 1

        return True
        
