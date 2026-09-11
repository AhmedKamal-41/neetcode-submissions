class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        hashmap = {}

        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1

            most_freq = max(hashmap.values())

            while (r - l + 1) - most_freq > k:
                hashmap[s[l]] -= 1
                l += 1
                most_freq = max(hashmap.values())

            longest = max(longest, r - l + 1)

        return longest