"""Description
Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the 
island. If two 1 is adjacent, we consider them in the same island. We only 
consider up/down/left/right adjacent.

Find the number of islands.
"""

"""Example
Example 1:

    Input:
    [
        [1,1,0,0,0],
        [0,1,0,0,1],
        [0,0,0,1,1],
        [0,0,0,0,0],
        [0,0,0,0,1]
    ]
    Output:
    3

Example 2:

    Input:
    [
        [1,1]
    ]
    Output:
    1
"""

"""Related Problems

"""

"""433. Number of Islands
Tags: BFS & Union Find
"""
from collections import deque

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
            
        islands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    islands += 1
                    
        return islands                    
    
    def bfs(self, grid, x, y, visited):
        queue = deque([(x, y)])
        visited.add((x, y))
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.is_valid(grid, next_x, next_y, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))

    def is_valid(self, grid, x, y, visited):
        n, m = len(grid), len(grid[0])
        if not (0 <= x < n and 0 <= y < m):
            return False
        if (x, y) in visited:
            return False
        return grid[x][y]
