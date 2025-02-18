def position_check(queen_position, q):
    k = len(queen_position)
    if k == 0:
        return True
    for i in range(k):
        if q-(i+1) == queen_position[k-1-i] or q+(i+1) == queen_position[k-1-i] or q == queen_position[k-1-i]:
            return False
    return True


def recQueen(n, queen_position, y):
    global count
    if y == n:
        count += 1
        return 
    for i in range(n):
        if position_check(queen_position, i):
            new = queen_position + [i]
            recQueen(n, new, y+1)
        else:
            continue
    
    
        



count = 0
n = int(input())
queen_position = []
recQueen(n, queen_position, 0)
print(count)
