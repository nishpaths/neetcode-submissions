class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top_row = 0
        bottom_row =  len(matrix) - 1
        mid_row = 0
        while top_row <= bottom_row:
            mid_row = (top_row + bottom_row)//2
            if matrix[mid_row][-1] < target:
                top_row = mid_row + 1
            elif matrix[mid_row][0] > target:
                bottom_row = mid_row - 1
            else:
                break

        if top_row > bottom_row:
            return False 
        left = 0
        right = len(matrix[mid_row]) - 1
        mid = (left + right) // 2
        while left <= right:
            mid = (left + right)//2
            if matrix[mid_row][mid] == target:
                return True
            elif matrix[mid_row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False