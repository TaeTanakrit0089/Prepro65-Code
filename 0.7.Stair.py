"Gustavo Fring"
import sys

x = int(input())
y = x

for line in range(1,y+1):
    for num in range(1,line+1):
        print(num, end = '')
        num +=1
    line += 1
    print("")