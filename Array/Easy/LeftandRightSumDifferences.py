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
