class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        for n in nums:
            if min(n, result) == n:
                result = n
        return result
