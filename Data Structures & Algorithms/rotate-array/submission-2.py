class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #k = k % len(nums) # the rotation can be looped over and over and gives the same results to loop for the needed rotation by (rotation by len does notthing so rotation by 5 is the same as 2)

        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]