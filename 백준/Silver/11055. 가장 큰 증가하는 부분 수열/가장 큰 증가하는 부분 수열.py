# 가장 큰 증가하는 부분 수열 복습

n = int(input())
arr = list(map(int, input().split()))

dp = [0 for _ in range(n)]

dp[0] = arr[0]

for i in range(1,n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[j] + arr[i], dp[i])
        else:
            dp[i] = max(dp[i],arr[i])

print(max(dp))