class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_array = []
        for num in nums:
            if num in nums_array:
                return num
            else:
                nums_array.append(num)