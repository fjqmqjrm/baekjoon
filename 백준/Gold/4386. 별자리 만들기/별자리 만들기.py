import math 

def find(x):
    while par[x] != x:
        x = par[x]
    return x
def union(n1, n2):
    n1 = find(n1)
    n2 = find(n2)

    if n1 == n2:
        return
    
    if rank[n1] < rank[n2]:
        par[n1] = n2
    elif rank[n2] < rank[n1]:
        par[n2] = n1
    else:
        par[n2] = n1
        rank[n1] += 1


n = int(input())
points = [list(map(float, input().split())) for _ in range(n)]
link = []
rank = [0 for _ in range(n)]
par = [i for i in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            link.append([i, j, math.sqrt((points[i][0]-points[j][0])**2 + ((points[i][1]-points[j][1])**2))])


link.sort(key = lambda x : x[2])
ans = 0
#node = [False] * n
for i in range(len(link)):
    '''if node == [True] * n:
        break'''
    num1, num2, wei = link[i][0], link[i][1], link[i][2] 
    num1, num2 = find(num1), find(num2)
    
    if num1 == num2:
        continue
    else:
        union(num1, num2)
        #node[num1], node[num2] = True, True
        ans += wei
if n == 1:
    ans = 0
print(round(ans, 2))