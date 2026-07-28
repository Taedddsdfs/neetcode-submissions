class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def dfs(row, col, size):
            first = grid[row][col]
            same = True

            # 현재 구역 검사
            for r in range(row, row + size):
                for c in range(col, col + size):
                    if grid[r][c] != first:
                        same = False

            # 전부 같은 숫자
            if same:
                return Node(first, True, None, None, None, None)

            # 숫자가 섞여 있음 → 4등분
            half = size // 2

            return Node(
                1,
                False,
                dfs(row, col, half),                       # 왼쪽 위
                dfs(row, col + half, half),                # 오른쪽 위
                dfs(row + half, col, half),                # 왼쪽 아래
                dfs(row + half, col + half, half)          # 오른쪽 아래
            )

        return dfs(0, 0, len(grid))