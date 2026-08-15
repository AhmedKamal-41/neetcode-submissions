class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        entry_list = list(hashmap.items())
        entry_list.sort(key=lambda x: x[1], reverse=True)

        return list(map(lambda x: x[0], entry_list[:k]))