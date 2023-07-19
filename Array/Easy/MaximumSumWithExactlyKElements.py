# You are given a 0-indexed integer array nums and an integer k. Your task is to perform the following operation exactly k times in order to maximize your score:

# Select an element m from nums.
# Remove the selected element m from the array.
# Add a new element with a value of m + 1 to the array.
# Increase your score by m.
# Return the maximum score you can achieve after performing the operation exactly k times.

class Solution(object):
    def maximizeSum(self, nums, k):
        total = 0
        nums.sort()
        element = nums[-1]
        while (k):
            total += element
            element += 1
            k -= 1
        return total


result = Solution().maximizeSum([1, 2, 3, 4, 5], 3)
print(result)
