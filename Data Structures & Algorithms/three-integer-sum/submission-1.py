class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for start in range(len(nums)):
            if start > 0 and nums[start] == nums[start - 1]:
                continue

            target = -nums[start]

            i = start + 1
            j = len(nums) - 1

            while i < j:
                current = nums[i] + nums[j]

                if current > target:
                    j -= 1

                elif current < target:
                    i += 1

                else:
                    result.append([nums[start], nums[i], nums[j]])

                    i += 1
                    j -= 1

                    while i < j and nums[i] == nums[i - 1]:
                        i += 1

                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1

        return result 