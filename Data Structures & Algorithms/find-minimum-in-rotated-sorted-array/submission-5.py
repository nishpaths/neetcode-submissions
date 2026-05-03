class Solution:
    def findMin(self, nums: List[int]) -> int:
       l = 0
       r = len(nums) - 1
       while l <= r:
        if nums[l] <= nums[r]:
            return nums[l]
        else:
            l = l + 1

            
