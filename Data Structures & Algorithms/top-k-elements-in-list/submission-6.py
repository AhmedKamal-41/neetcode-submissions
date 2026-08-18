class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1
        
        result_list = list(hashmap.items())
        result_list.sort(key=lambda x: x[1], reverse=True)

        return list(map(lambda x: x[0], result_list[:k]))