import heapq
n = int(input())
heap = []
for _ in range(n):
    num = int(input())
    heapq.heappush(heap, num)

ans = 0
if n == 1:
    heap = [0]
a = 0
b = 0
while len(heap) != 1:
    ans += (a+b)
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    heapq.heappush(heap, a+b)



print(heap[0] + ans)
