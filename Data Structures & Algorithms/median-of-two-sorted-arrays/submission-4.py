class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)

        if len(nums) % 2 == 1:
            return nums[(len(nums)-1)//2]
        else:
            mid = (len(nums)-1)//2
            median = (nums[mid] + nums[mid + 1]) / 2
            return median
            
        