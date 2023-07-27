# You are given an n x n integer matrix grid.
# Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:
# maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
# In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

# Return the generated matrix.

class Solution(object):
    def largestLocal(self, grid):
        resultMatrix = [[0 for line in range(
            len(grid) - 2)] for col in range(len(grid)-2)]
        for i in range(len(grid)-2):
            for j in range(len(grid)-2):
                resultMatrix[i][j] = max(
                    grid[i][j], grid[i][j+1], grid[i][j+2],
                    grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                    grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2])
        return resultMatrix


result = Solution().largestLocal(
    [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
print(result)
