def find(k):
    global n
    if len(k) == n:
        print(k)
        exit()
    for i in ['1','2','3']:
        if check_num(k+i):
            find(k+i)
        else:
            continue
    
    
def check_num(num):
    l = len(num)
    for i in range(len(num)//2):
        if num[l-1-i:] == num[l-1-i-i-1:l-1-i]:
            return False

        
    return True

n = int(input())
find('1')
