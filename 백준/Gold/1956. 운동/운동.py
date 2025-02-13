

V, E = map(int, input().split())
dist = [[1e9]*(V+1)  for _ in range(V+1)]


for i in range(E):
    startNode, endNode, edge = map(int, input().split())
    dist[startNode][endNode] = edge

for i in range(1, V+1):
    for j in range(1, V+1):
        for k in range(1, V+1):
            if dist[j][i] != 1e9 and dist[i][k] != 1e9:
                dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])


ans = 1e9

for i in range(1, V+1):
    ans = min(ans, dist[i][i])

if ans == 1e9:
    print(-1)
else:
    print(ans)


