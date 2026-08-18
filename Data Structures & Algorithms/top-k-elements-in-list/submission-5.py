class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1
        
        return list(sorted(hashmap,key=hashmap.get,reverse=True)[:k])