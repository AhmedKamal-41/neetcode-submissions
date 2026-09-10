class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]: #skips to use the same element again because in sorted array you will go through the same conditions this avoids -0 and [0,0,0,0] repeating problem
                continue

            l = i + 1
            r = len(nums) - 1

            target = -nums[i]

            while r > l:
                if nums[r] + nums[l] == target:
                    result.append([nums[i], nums[l], nums[r]])
                    #break --> not optimal it with the first comment it will skip another group so to solve it
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif nums[r] + nums[l] > target:
                    r -= 1

                else:
                    l += 1

        return result