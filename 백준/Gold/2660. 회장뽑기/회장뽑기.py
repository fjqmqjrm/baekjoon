from collections import deque
n = int(input())
links = [[] for _ in range(n+1)]
scores = [0 for _ in range(n+1)]

while True:
    per1, per2 = map(int, input().split())
    if per1 == -1 and per2 == -1:
        break
    links[per1].append(per2)
    links[per2].append(per1)


def getScoreBfs(perNum):
    global n
    visited = [False] * (n+1) 
    queue = deque([(perNum, 0)]) 
    visited[perNum] = True
    score = 0
    while queue:
        pointPer, perScore  = queue.popleft()
        score = perScore
        for per in links[pointPer]:
            if not visited[per]:
                queue.append((per, perScore+1))
                visited[per] = True


    return score


for i in range(1,n+1):
    scores[i] = getScoreBfs(i)

minScore = min(scores[1:])
countMinPer = 0
ansPer = []
for i in range(1, len(scores)):
    if scores[i] == minScore:
        countMinPer += 1
        ansPer.append(i)

print(minScore, countMinPer)
print(*ansPer)