class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        best_area = 0
        i = 0
        j = len(heights) - 1
        
        while i < j:

            width = j - i
            high = min(heights[i], heights[j])
            area = width * high

            if area > best_area:
                best_area = area
            
            if heights[i] <= heights[j]:
                i+=1
            else:
                j-=1
        return best_area
            

