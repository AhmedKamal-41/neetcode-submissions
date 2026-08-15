class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups_map = {}

        for words in strs:
            key = ''.join(sorted(words))

            if key not in groups_map:
                groups_map[key] = []
            
            groups_map[key].append(words)

        return list(groups_map.values())