from itertools import permutations

k = int(input())
p = input().split()
numbers = [0,1,2,3,4,5,6,7,8,9]

def check_num(numLi):
    check = []
    for i in range(k):
        if numLi[i] < numLi[i+1]:
            check.append('<')
        else:
            check.append('>')
    if p == check:
        return True
    else:
        return False

numsets = permutations(numbers, k+1)
ok = []
for numset in numsets:
    if check_num(numset):
        ok.append(numset)
    else:
        continue
maxans = ""
minans = ""
for num in max(ok):
    maxans += str(num)
for num in min(ok):
    minans += str(num)

print(maxans)
print(minans)

