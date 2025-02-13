import sys
sys.setrecursionlimit(10**5)

n, m, r = map(int, input().split())
graph  = [[]for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for node in graph:
    node.sort(reverse = True)

count = 1
visited = [False] * (n+1)
ans = [0 for _ in range(n+1)]


def dfs(node, graph):
    global visited, count, ans
    
    for n in graph[node]:
        if visited[n] == False:
            visited[n] = True
            count += 1
            ans[n] = count
            dfs(n, graph)
    return

visited[r] = True
ans[r] = 1
dfs(r, graph)
for i in range(1, n+1):
    print(ans[i])
