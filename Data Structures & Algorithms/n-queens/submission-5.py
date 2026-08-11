class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [("." * n) for _ in range(n)]
        result = []

        def valid(r, c):
            if "Q" in grid[r]:
                return False

            row, col = r, c

            while r >= 0 and c >= 0:
                if grid[r][c] == "Q":
                    return False
                r -= 1
                c -= 1

            r, c = row, col

            while r < n and c >= 0:
                if grid[r][c] == "Q":
                    return False
                r += 1
                c -= 1

            return True

        def queens(c):
            if c == n:
                result.append(grid[:])
                return 

            for r in range(n):
                if valid(r, c):
                    grid[r] = grid[r][:c] + "Q" + grid[r][c+1:]
                    queens(c+1)
                    grid[r] = grid[r][:c] + "." + grid[r][c+1:]

        queens(0)
        return result
                

        