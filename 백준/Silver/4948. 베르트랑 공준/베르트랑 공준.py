from math import *


ans = []
while True :
    number = int(input())
    if number == 0:
        break
    check = int(sqrt(2*number)+1)
    numbers = [False for i in range(123456*2+1)]
    numbers[1] = True
    numbers[2] = False
   
    for num in range(2,check):
        for o in range(2, (2*number)//num+1):
            numbers[num*o] = True
           
    count = 0
    for num in range(number+1, 2*number+1):
        if numbers[num] == False:
            count += 1
            
        
    ans.append(count)
    

print(*ans, sep = '\n')

