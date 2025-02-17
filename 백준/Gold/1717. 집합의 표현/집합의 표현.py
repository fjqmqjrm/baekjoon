def union(num1, num2):
    root1 = find(num1)
    root2 = find(num2)
    if root1 != root2:
        parents[root2] = root1

def find(num1):
    if num1 == parents[num1]:
        return num1
    else:
        parents[num1] = find(parents[num1]) 
    return parents[num1] 

n, m = map(int, input().split())
links = [[] for _ in range(n+1)]
parents = [i for i in range(n+1)]
ans = []
for _ in range(m):
    check, n1, n2 = map(int, input().split())
    if check == 0:
        union(n1, n2)
    if check == 1:  
        if find(n1) == find(n2):
            ans.append('YES')
        else:
            ans.append('NO')
print(*ans, sep = '\n')


