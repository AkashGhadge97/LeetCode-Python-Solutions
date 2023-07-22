# Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

class Solution(object):
    def maxProduct(self, nums):
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)

result = Solution().maxProduct([1, 5, 4, 5])
print(result)
