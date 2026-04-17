# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        estimate = 1
        while left <= right:
            estimate = (right - left)//2 + left
            g = guess(estimate)
            if g == 0:
                return estimate
            elif g < 0:
                right = estimate - 1
            else:
                left = estimate + 1
        return -1