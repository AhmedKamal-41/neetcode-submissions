class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        l = 0

        diff = max(nums[l:k]) - min(nums[l:k])

        for r in range(k, len(nums)):
            l+=1
            
            difference = max(nums[l:r+1]) - min(nums[l:r+1])
            
            diff = min(diff, difference)

        return diff