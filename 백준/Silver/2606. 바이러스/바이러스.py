N = int(input())
M = int(input())

graph =[[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)
    
def recur(node):

    visited[node] = True

    for nxt in graph[node]:
        if not visited[nxt]:
            recur(nxt)

recur(1)
print(visited.count(True)-1)