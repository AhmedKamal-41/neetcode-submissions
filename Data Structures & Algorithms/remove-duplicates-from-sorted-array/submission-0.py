class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i):
                if nums[i] == nums[j]:
                    nums.pop(i)
                    break

        return len(nums)