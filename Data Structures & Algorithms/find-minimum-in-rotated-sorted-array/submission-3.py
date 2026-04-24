class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        result = nums[0]
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= nums[l]:
                result = min(result,  nums[l])
                l = mid + 1
            else:
                result = min(result, nums[mid])
                r = mid - 1
        return result
            
