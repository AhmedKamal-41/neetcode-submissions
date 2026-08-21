class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums) # intial value for each is 1  -  the len is the same as nums
        product = 1
        
        for i in range(len(nums)):
            output[i] = product
            product *= nums[i]

        product = 1
        
        for i in range(len(nums)-1, -1, -1):
            output[i] *= product
            product *= nums[i]
        
        return output

