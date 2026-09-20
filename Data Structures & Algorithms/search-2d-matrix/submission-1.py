class Solution:
   def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    l = 0
    r = len(matrix) - 1

    while r >= l:
        mid_arr = ((l + r) + 1) // 2

        if target < matrix[mid_arr][0]:
            r = mid_arr - 1

        elif target > matrix[mid_arr][-1]:
            l = mid_arr + 1

        else:
            left = 0
            right = len(matrix[mid_arr]) - 1

            while right >= left:
                mid = ((left + right) + 1) // 2

                if target == matrix[mid_arr][mid]:
                    return True

                elif target > matrix[mid_arr][mid]:
                    left = mid + 1

                else:
                    right = mid - 1

            return False

    return False