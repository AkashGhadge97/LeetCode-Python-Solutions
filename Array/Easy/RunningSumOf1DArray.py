# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.


class Solution(object):
    def runningSum(self, nums):
        final = []
        total = 0
        for i in nums:
            total += i
            final.append(total)
        return final

result = Solution().runningSum([1, 2, 3, 4])
print(result)
