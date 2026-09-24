class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        results = []
        product = 1

        for i in range(len(nums)):
            prefix[i] = product
            product *= nums[i]
        
        product = 1

        for i in range(len(nums)-1, - 1 , -1):
            postfix[i] = product
            product *= nums[i]

        for i in range(len(nums)):
            results.append(postfix[i] * prefix[i])
        
        return results 