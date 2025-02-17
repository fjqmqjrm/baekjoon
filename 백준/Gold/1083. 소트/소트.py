
def point(idx, namNum):
    global n
    if idx + namNum +1 < n:
        top_num = max(arr[idx:idx+namNum+1])
    else:
        top_num = max(arr[idx:n])
    top_num_idx = arr.index(top_num)
    namNum = namNum - (top_num_idx-idx)
    pt1, pt2 = top_num_idx-1, top_num_idx

    # 가장 큰 놈 보내기
    while pt1 >= idx:
        num1, num2 = arr[pt1], arr[pt2]

        arr[pt1], arr[pt2] = num2, num1
        pt1 -= 1
        pt2 -= 1
    #print(idx, namNum, top_num)
    return namNum

n = int(input())
arr = list(map(int, input().split()))
s = int(input())
cnt = 0

# 가장 큰 놈을 최대한 빨리 앞으로 보낸다 
top_num = max(arr[0:s+1])
top_num_idx = arr.index(top_num)
nam = s - top_num_idx
pt1, pt2 = top_num_idx-1, top_num_idx
idx = 1
# 가장 큰 놈 보내기
while pt1 >= 0:
    num1, num2 = arr[pt1], arr[pt2]

    arr[pt1], arr[pt2] = num2, num1
    pt1 -= 1
    pt2 -= 1
    
while nam >= 0 and idx < n:
    nam = point(idx, nam)
    idx += 1
    

print(*arr)


