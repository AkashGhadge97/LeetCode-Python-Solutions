# Given a square matrix mat, return the sum of the matrix diagonals.

# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

class Solution(object):
    def diagonalSum(self, mat):
        total = 0
        for i in range(0, len(mat)):
            total += mat[i][i]
        for i in range(len(mat), 0, -1):
            if ((i-1) == len(mat) - i):
                continue
            total += mat[i-1][len(mat)-i]
        return total


result = Solution().diagonalSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(result)
