class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = "".join(char for char in s.lower() if char.isalnum())
        right = left[::-1]
        return left == right