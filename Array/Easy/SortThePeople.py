# You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.
# For each index i, names[i] and heights[i] denote the name and height of the ith person.
# Return names sorted in descending order by the people's heights.


class Solution(object):
    def sortPeople(self, names, heights):
        pdict = {}
        for i, j in zip(heights, names):
            pdict[i] = j
        keysArray = sorted(pdict.keys())[::-1]
        return [pdict[i] for i in keysArray]


result = Solution().sortPeople(["Mary", "John", "Emma"], [180, 165, 170])
print(result)
