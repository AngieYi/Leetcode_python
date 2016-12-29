'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
'''

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        L1 = len(grid)
        L2 = len(grid[0])
        sum = 0
        for i in xrange(L1):
            for j in xrange(L2):
                if grid[i][j] == 1:
                    temp = 4
                    if i != 0 and grid[i-1][j] == 1:    # top
                        temp -= 1
                    if i != L1-1 and grid[i+1][j] == 1:  # buttom
                        temp -= 1
                    if j != 0 and grid[i][j-1] == 1:    # left
                        temp -= 1
                    if j != L2-1 and grid[i][j+1] == 1:  # right
                        temp -= 1
                    sum += temp
        return sum