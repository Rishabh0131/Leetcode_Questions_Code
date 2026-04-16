from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()  # can be removed

        def dfs(i, j):

            if (i, j) in visited:
                return

            if (
                i < 0
                or j < 0
                or i >= len(grid)
                or j >= len(grid[0])
                or grid[i][j] == "0"
            ):
                return

            visited.add((i, j))  # replace -> grid[i][j] = "0"

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

            return

        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][
                    j
                ] == "1":  # remove visited conditon
                    dfs(i, j)
                    res += 1

        return res
