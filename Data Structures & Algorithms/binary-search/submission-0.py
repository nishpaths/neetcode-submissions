class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while(left <= right):
            midpoint = (left + right)//2
            num = nums[midpoint]
            if num == target:
                return midpoint
            elif num < target:
                left = midpoint + 1
            else:
                right = midpoint - 1
        return -1
