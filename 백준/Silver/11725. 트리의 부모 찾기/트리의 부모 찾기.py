import sys

sys.setrecursionlimit(10**5)

def find_parents(root_node):
    visited[root_node] = True
    for node in links[root_node]:
        if not visited[node]:
            parents[node] = root_node
            find_parents(node)
    return



n = int(input())
links = [[] for _ in range(n+1)]
parents = [i for i in range(n+1)]
visited = [False] * (n+1)
for _ in range(n-1):
    node1, node2 = map(int, input().split())
    links[node1].append(node2)
    links[node2].append(node1)

find_parents(1)
print(*parents[2:], sep = '\n')
