import numpy as np
from collections import deque


def capture_territory(grid , player_id):
    blocked = ((grid == player_id) | (grid == -player_id))
    visited = np.zeros_like(blocked , dtype = bool)
    rows, cols = grid.shape
    q = deque()
    for r in range(rows):
        for c in [0 , cols - 1]:
            if not blocked[r ,c]:
                
                q.append((r ,c))
                visited[r,c] = True 
    for c in range(cols):
        for r in [0, rows - 1]:

            if not blocked[r, c]:
                q.append((r, c))
                visited[r, c] = True
    directions = [(1,0) , (0,1),(-1,0),(0,-1)]
    while q:
         r , c = q.popleft()
         for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if (
                 0 <= nr < rows
                 and 0 <= nc < cols
                 and not blocked[nr, nc]
                 and not visited[nr, nc]
            ): 
                visited[nr,nc] = True
                q.append((nr,nc))
               
    enclosed = (~visited) & (~blocked)
    grid[enclosed] = player_id
    grid[grid == -player_id] = player_id