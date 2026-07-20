from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        total = rows * cols
        k %= total

        ans = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                # Convert 2D index to 1D
                idx = i * cols + j

                # Find new index after shifting
                new_idx = (idx + k) % total

                # Convert new 1D index back to 2D
                r = new_idx // cols
                c = new_idx % cols

                ans[r][c] = grid[i][j]

        return ans