#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. T.C = O(logn)
class Solution(object):
   def searchInsert(self, nums, target):
        lower = 0
        upper = len(nums)
        while (lower < upper):
            mid = int((lower+upper)/2)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                lower = mid + 1
            else:
                upper = mid
        return lower
