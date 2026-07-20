from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        arr = []
        for row in grid:
            arr.extend(row)

        total = len(arr)
        k %= total

        arr = arr[-k:] + arr[:-k]

        ans = []
        for i in range(0, total, cols):
            ans.append(arr[i:i + cols])

        return ans