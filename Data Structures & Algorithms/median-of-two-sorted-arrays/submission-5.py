class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        if len(nums1) > len(nums2):
            A = nums2
            B = nums1
        left_size = (len(A) + len(B) + 1)//2
        l = 0
        r = len(A)
        while l <= r:
            i = (l+r)//2
            j = left_size - i
            A_left = A[i-1] if i > 0 else float('-inf')
            A_right = A[i] if i < len(A) else float('inf')
            B_left = B[j-1] if j > 0 else float('-inf')
            B_right = B[j] if j < len(B) else float('inf')

            if A_left <= B_right and B_left <= A_right:
                if (len(A) + len(B)) % 2 == 1:
                    return max(A_left, B_left)
                else:
                    return (min(A_right, B_right) + max(A_left, B_left))/2
            elif A_left > B_right:
                r = i - 1
            elif B_left > A_right:
                l = i + 1
            

        