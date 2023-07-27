# Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

# The value of |x| is defined as:

# x if x >= 0.
# -x if x < 0.

class Solution(object):
    def countKDifference(self, nums, k):
        return sum(nums.count(num+k) for num in nums if num+k in nums)

result = Solution().countKDifference([1, 2, 2, 1], 1)
print(result)
