import heapq


maxheap = []
minheap = []
ans = []
n = int(input())
if n == 1:
    print(int(input()))
elif n == 2:
    n1 = int(input())
    n2 = int(input())
    if n1 > n2:
        print(n2)
    else:
        print(n1)
else:
    n1 = int(input())
    ans.append(n1)
    n2 = int(input()) 
    if n1 > n2:
        maxheap = [-n2]
        minheap = [n1]
    else:
        maxheap = [-n1]
        minheap = [n2]
    ans.append(-maxheap[0])
    for _ in range(n-2):
        number = int(input())
        maxL, minL = len(maxheap), len(minheap)
        if maxL == minL:
            if minheap[0] < number:
                heapq.heappush(maxheap, -heapq.heappop(minheap))
                heapq.heappush(minheap, number)
            else:
                heapq.heappush(maxheap, -number) 
        elif maxL == minL+1:
            if -maxheap[0] < number:
                heapq.heappush(minheap, number)
            else:
                heapq.heappush(minheap, -heapq.heappop(maxheap))
                heapq.heappush(maxheap, -number)
        
        ans.append(-maxheap[0])
        
        
for num in ans:
    print(num)
    

    
