# Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

# answer.length == nums.length.
# answer[i] = |leftSum[i] - rightSum[i]|.
# Where:

# leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
# rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
# Return the array answer.

import math

class Solution(object):
    def leftRightDifference(self, nums):
        resultList = []
        for i in range(0, len(nums)):
            if i == 0:
                resultList.append(abs(0-sum(nums[(i+1):])))
            else:
                resultList.append(abs(sum(nums[(i-1)::-1])-sum(nums[(i+1):])))
        return resultList
