# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

class Solution(object):
    def largestAltitude(self, gain):
        al = 0
        max_al = 0
        for i in gain:
            al += i
            max_al = max(al, max_al)
        return max_al


result = Solution().largestAltitude([-5, 1, 5, 0, -7])
print(result)
