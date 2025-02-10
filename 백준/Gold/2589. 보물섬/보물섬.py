from collections import deque

H, W = map(int, input().split())
graph = [list(input()) for _ in range(H)]


def bfs(x, y):
    visited = [[False for _ in range(W)] for _ in range(H)]
    dist = [[0 for _ in range(W)] for _ in range(H)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    max_dist = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < H and 0 <= ny < W and graph[nx][ny] == 'L' and not visited[nx][ny]:
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                max_dist =  max(max_dist, dist[nx][ny])
                q.append((nx,ny))

        
    return max_dist

max_result = 0
for i in range(H):
    for j in range(W):
        if graph[i][j] == 'L': 
            max_result = max(max_result, bfs(i, j))

print(max_result)