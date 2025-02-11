from collections import deque


def bfs():
    global X, Y
    visited = [[False]*X for _ in range(Y)]

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    queue = deque()

    for y in range(Y):
        for x in range(X):
            if box[y][x] == 1:
                queue.append((y,x,0))
                visited[y][x] = True
    
    while queue:
        ny, nx, day = queue.popleft()
        visited[ny][nx] = True

        for i in range(4):
            cy, cx = ny + dy[i], nx + dx[i]
            if 0 <= cy < Y and 0<= cx < X and not visited[cy][cx] and box[cy][cx] == 0:
                visited[cy][cx] = True
                box[cy][cx] = 1
                queue.append((cy,cx,day+1))
                
        if not queue:
            return day
        
     

            
X, Y = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(Y)]

day = bfs()

if any(0 in row for row in box):
    print(-1)
else:   
    print(day)


