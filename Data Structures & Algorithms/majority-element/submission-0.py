class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        n = len(nums) / 2

        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
        
        for key in hashmap:
            if hashmap[key] >= n:
                return key
    
            