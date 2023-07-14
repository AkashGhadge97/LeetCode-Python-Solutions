# You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

# i < j < k,
# nums[j] - nums[i] == diff, and
# nums[k] - nums[j] == diff.
# Return the number of unique arithmetic triplets.

class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        result = []
        for i in range(0, len(nums)):
            if ((nums[i] + diff) in nums and (nums[nums.index(nums[i]+diff)] + diff) in nums):
                result.append([i, nums.index(nums[i]+diff),
                              nums.index(nums[nums.index(nums[i]+diff)] + diff)])
        return len(result)


result = Solution().arithmeticTriplets([4, 5, 6, 7, 8, 9], 2)
print(result)
