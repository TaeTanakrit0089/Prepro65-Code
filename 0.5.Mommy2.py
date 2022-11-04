import sys

x = int(input())
y = int(input())
sum = 0
for i in range(sys.maxsize**10):
    if(i == 0):
        continue
    if(i == y+1):
        break
    print(x, "X", i, "=", x*i)
    sum += x*i
print("Sum =", sum)
