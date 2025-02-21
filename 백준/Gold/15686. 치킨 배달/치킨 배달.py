from itertools import combinations

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

def mChickens(chickens, m):
    return list(combinations(chickens, m))
    

chickens = []
homes = []
mchickens = []

for y in range(n):
    for x in range(n):
        if city[y][x] == 1:
            homes.append([y,x])
        elif city[y][x] == 2:
            chickens.append([y,x])

mchickens = mChickens(chickens, m)

def getchickenDistance(mchicken, homes):
    chickenDistance = 0
    for home in homes:
        thisHomeDistance = 1e9
        for chicken in mchicken:
            thisHomeDistance = min(thisHomeDistance, abs(home[0]-chicken[0]) + abs(home[1]-chicken[1]))
        chickenDistance += thisHomeDistance
    return chickenDistance

ans = 1e9

for mchicken in mchickens: # 치킨집 조합 마다
    ans = min(ans,getchickenDistance(mchicken, homes))

print(ans)
        
    
      


