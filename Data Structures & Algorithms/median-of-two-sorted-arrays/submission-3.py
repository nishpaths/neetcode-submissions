class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums = sorted(nums)
        l,r = 0, len(nums) - 1
        mid = (l + r) // 2
        if len(nums) % 2 == 1:
            return nums[mid]
        else:
            return (nums[mid] + nums[mid + 1]) /2