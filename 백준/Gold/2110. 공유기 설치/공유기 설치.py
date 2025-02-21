n, c = map(int, input().split())
homes = [int(input()) for _ in range(n)]
homes.sort() 

low, high = 1, homes[n-1] - homes[0] + 1 

def findInstallNum(num):
    count = 1
    la = 0
    for i in range(1, n):
        if homes[i] - homes[la] >= num :
            la = i
            count += 1
    return count 

while low < high:
    mid = (low + high) // 2
    if findInstallNum(mid) < c:
        high = mid
    else:
        low = mid + 1
print(low-1)
    

    








