from math import *
# 1은 소수 아님
def getPrimeNums(number):
    numLi = [True for i in range(number+1)]
    numLi[0], numLi[1] = False, False
    for i in range(2,int(sqrt(number))+1):
        for j in range(2, number//i+1):
            numLi[i*j] = False
    return numLi

n = int(input())
primeNumbersTF = getPrimeNums(n)
primeNumbers = []
for i in range(len(primeNumbersTF)):
    if primeNumbersTF[i]:
        primeNumbers.append(i)


count = 0

start, end = 0,0

while 0<= start < len(primeNumbers) and 0 <= end <= len(primeNumbers):
    if sum(primeNumbers[start:end+1]) < n:
        end += 1
    elif sum(primeNumbers[start:end+1]) > n:
        start += 1
        end = start 
    else:
        count += 1
        start += 1
        end = start
    

print(count)
