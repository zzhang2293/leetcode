from collections import deque
def minMoves(n: int, startRow: int, startCol: int, endRow: int, endCol: int) -> int:
    moves = [(2, 1), (-2, 1), (1, 2), (-1, 2), (2, -1), (-2, -1), (1, -2), (-1, -2)]
    queue = deque([(startRow, startCol, 0)])
    visited = {startRow, startCol}
    while queue:
        x, y, count = queue.popleft()
        if x == endRow and y == endCol:
            return count
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, count + 1))

    return float('inf')
print(minMoves(9, 4, 4, 4, 8))
