def find(x):
    while par[x] != x: 
        x = par[x]
    return x 

def union(a,b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    
    if rank[a] < rank[b]:
        par[a] = b

    elif rank[b] < rank[a]:
        par[b] = a

    else:
        par[a] = b
        rank[b] += 1



n, m  = map(int, input().split())

link = [list(map(int, input().split())) for _ in range(m)]
par =  [i for i in range(n+1)]
rank = [0 for _ in range(n+1)]
link.sort(key = lambda x : x[2]) # 가중치 기준 정렬


ans =  0

for i in range(m):
    n1, n2, weight = link[i][0], link[i][1], link[i][2] 
    
    n1 = find(n1)
    n2 = find(n2)

    if n1 != n2:
        union(n1, n2)
        ans += weight
    else:
        continue

print(ans)

        
