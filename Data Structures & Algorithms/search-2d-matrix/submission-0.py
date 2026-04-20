class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        unpacked =  [item for row in matrix for item in row]
        left = 0
        right = len(unpacked) - 1
        while left <= right:
            mid = (left + right)//2
            if unpacked[mid] == target:
                return True
            elif unpacked[mid] < target:
                left = mid + 1 
            else:
                right = mid - 1
        return False