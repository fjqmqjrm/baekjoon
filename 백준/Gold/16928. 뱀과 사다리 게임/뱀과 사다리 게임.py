from collections import deque

sa, be = map(int, input().split())

links = [[j for j in range(i+1,i+7) if j <= 100] for i  in range(101)]
sa_or_bem  = [False] * 101
for _ in range(sa):
    start, end = map(int, input().split())
    links[start] = [end]
    sa_or_bem[start] = True

for _ in range(be):
    start, end = map(int, input().split())
    links[start] = [end]
    sa_or_bem[start] = True


def bfs(links, start):
    queue = deque()
    count = 0
    queue.append((start,count))
    visited = [False] * 101
    visited[start] = True
    while queue:
        this_node, co = queue.popleft()
        
        if this_node == 100:
            return co
        for node in links[this_node]:
             
             if not visited[node]:  
                  

                next_pos = node
                while sa_or_bem[next_pos]:  
                    next_pos = links[next_pos][0]  

                if not visited[next_pos]: 
                    visited[next_pos] = True  
                    queue.append((next_pos, co + 1))  
            
print(bfs(links, 1))



