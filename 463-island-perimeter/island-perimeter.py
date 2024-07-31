class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int) -> int:
            # Basecase 1: for out of bound items, return 1, because the boundary of the square suggest perimeter
            if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[i])-1:
                return 1
            # Basecase 2: for water, return 1, because this side is a perimeter
            elif grid[i][j] == 0:
                return 1
            # Basecase 3: for '-1' return 0, because we have been there, this is land that we have accounted for
            elif grid[i][j] == -1:
                return 0
            # Change the grid value to '-1' to mark it as visited and recursively return the perimeter of neighbors to get perimeter of all neighbors.
            else:
                grid[i][j] = -1
                return dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
            
        # Iterate over the grid
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # If a '1' is seen then "explore" the island from this '1' using dfs return perimeter 
                if grid[i][j] == 1:
                    return dfs(i, j)