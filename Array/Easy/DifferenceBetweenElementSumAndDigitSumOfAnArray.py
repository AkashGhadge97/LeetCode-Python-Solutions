# You are given a positive integer array nums.

# The element sum is the sum of all the elements in nums.
# The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
# Return the absolute difference between the element sum and digit sum of nums.

# Note that the absolute difference between two integers x and y is defined as |x - y|.

import math


class Solution(object):
    def differenceOfSum(self, nums):
        elementSum = sum(nums)
        digits = "".join([str(i) for i in nums])
        digitSum = sum([int(i) for i in digits])
        return abs(elementSum-digitSum)


result = Solution().differenceOfSum([1, 15, 6, 3])
print(result)
