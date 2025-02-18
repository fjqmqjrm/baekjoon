from collections import deque

H, W = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
# 공기 : -1 치즈 : 1 구멍 : 0
# 치즈 영역 크기 및 시간 초기화
ch_area, time = 0, 0
for b in board:
    ch_area += b.count(1)
board[0][0] = -1
# 공기화 
def to_air():
    global H, W
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    q = deque([(0,0)])
    visited = [[False] * W for _ in range(H)]
    while q:
        ny, nx = q.popleft()
       
        for i in range(4):
            cy, cx = ny + dy[i], nx + dx[i]

            if 0 <= cy < H and 0 <= cx < W and board[cy][cx] == 0 and not visited[cy][cx]:
                board[cy][cx] = -1
                q.append((cy, cx))
                visited[cy][cx] = True
            if 0 <= cy < H and 0 <= cx < W and board[cy][cx] == -1 and not visited[cy][cx]:
                q.append((cy, cx)) 
                visited[cy][cx] = True
        
    return

# 녹이기 - 0으로
def to_melt(ch_area):
    global H, W
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    q = deque([(0,0)])
    visited = [[False] * W for _ in range(H)]
    while q:
        ny, nx = q.popleft()

        for i in range(4):
            cy, cx = ny + dy[i], nx + dx[i]

            if 0 <= cy < H and 0 <= cx < W and board[cy][cx] == -1 and not visited[cy][cx]:
                q.append((cy, cx))
                visited[cy][cx] = True
            if 0 <= cy < H and 0 <= cx < W and board[cy][cx] == 1 and not visited[cy][cx]:
                visited[cy][cx] = True 
                board[cy][cx] = 0
                ch_area -= 1
    return ch_area


while 0 < ch_area:
    to_air()
    pre_area = ch_area
    ch_area = to_melt(pre_area)
    time += 1


print(time)
print(pre_area)



