class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        # Base case
        if grid[0][0] or grid[N-1][N-1]:
            return -1

        q = collections.deque([(0,0,1)])
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
        visited = set()

        while q:
            x,y,length = q.popleft()
            if x == N-1 and y ==N-1:
                return length
            for dx, dy in directions:
                nx,ny = x+dx, y+dy
                if (0<=nx<N and 0<=ny<N and (nx,ny) not in visited and grid[nx][ny]==0):
                    q.append((nx,ny,length +1))
                    visited.add((nx,ny))
        return -1