class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        found = {}

        for index , value in enumerate(nums):
            complement = target - value
            if complement in found:
                return [found[complement], index]
            found[value] = index