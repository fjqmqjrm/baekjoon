from collections import deque

k = int(input())
ans = []
            
def bfs(links, start):
    global visited
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        this_node = queue.popleft()

        for node in links[this_node]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)
    return 1

'''
for _ in range(k):
    count = 0
    v, e = map(int, input().split())
    links = [[] for _ in range(v+1)]
    visited = [False] * (v+1)
    for _ in range(e):
        node1, node2 = map(int, input().split())
      
        for notLinkedNode in range(v+1):
           
            if notLinkedNode != node1 and notLinkedNode != node2:
                links[node1].append(notLinkedNode)
                links[node2].append(notLinkedNode)
    
    for i in range(1, v+1):
        if not visited[i]:
            count += bfs(links,i)
    
    if count == 1 or count == 2:
        ans.append('YES')
    else:
        ans.append('NO')
    print(count)
            
for k in ans:
    print(k)'''

def reBfs(links, start):
    global teams
    queue = deque()
    queue.append((start,1))
    teams[start]= 1
    while queue:
        this_node, this_teamNum = queue.popleft()
        for node in links[this_node]:
            if teams[node] == 0: # 첫 방문 
                if this_teamNum == 1:
                    teams[node] = 2
                    queue.append((node,2))
                elif this_teamNum == 2:
                    teams[node] = 1
                    queue.append((node,1))
            elif teams[node] == this_teamNum:
                return False
            else:
                continue
    return True

            
for _ in range(k):
    count = 0
    team = 0
    v, e = map(int, input().split())
    links2 = [[] for _ in range(v+1)]
    teams = [0] * (v+1) # 팀 나누기 전 0 나눈후 1,2
    for _ in range(e):
        node1, node2 = map(int, input().split())
        links2[node1].append(node2)
        links2[node2].append(node1)
    flag = True
    m = 1
    for i in range(1, v+1):
        if teams[i] == 0:
            flag = reBfs(links2, i)
            if not flag:
                break
            
    print("YES" if flag else "NO")


    

    
   
            
