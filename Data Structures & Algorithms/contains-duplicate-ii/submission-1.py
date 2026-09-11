class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        l = 0

        for r in range(len(nums)):

            # check new element
            if nums[r] in seen:
                return True

            # add new element
            seen.add(nums[r])

            # keep window size limited to k
            if r - l >= k:
                seen.remove(nums[l])
                l += 1
        return False