class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for number in seen:
            if number - 1 not in seen:
                next_num = number + 1
                length = 1
                
                while next_num in seen:
                    next_num +=1
                    length +=1
                longest = max(longest, length)
        return longest
                