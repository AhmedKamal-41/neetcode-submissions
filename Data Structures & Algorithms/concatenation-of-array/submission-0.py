class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            ans.append(i)
        
        for i in nums:
            ans.append(i)

        return ans

        ''' another way
        for i in range(2):
            for num in nums:
                ans.append(num)
        '''