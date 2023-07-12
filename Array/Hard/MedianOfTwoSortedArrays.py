# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

import math

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        if (len(nums1) % 2 == 0):
            median = (nums1[int(len(nums1)/2)] + nums1[int(len(nums1)/2)-1])/2
        else:
            median = nums1[int(math.floor(len(nums1)/2))]
        return median


result = Solution().findMedianSortedArrays([1, 2], [3, 4])
print(result)
