class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COlS = len(grid[0])
        visit = set()
        q = deque()
        dist = 1
        for r in range(ROWS):
            for c in range(COlS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q:
            size = len(q)  # Store the initial size of the queue
            for _ in range(size):  # Iterate over the elements initially present in the queue
                r, c = q.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if row in range(ROWS) and col in range(COlS) and grid[row][col] == 2147483647 and (row, col) not in visit:
                        grid[row][col] = dist
                        q.append([row, col])
                        visit.add((row, col))
            dist += 1
