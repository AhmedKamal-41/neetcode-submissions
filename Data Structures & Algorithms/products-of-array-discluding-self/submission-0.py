class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        output = []
        zeros = nums.count(0)

        for num in nums:
            if num != 0:
                product *= num

        for num in nums:
            if zeros > 1:
                output.append(0)
            elif zeros == 1:
                if num == 0:
                    output.append(product)
                else:
                    output.append(0)
            else:
                output.append(product // num)

        return output