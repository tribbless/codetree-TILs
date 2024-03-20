import sys
input = sys.stdin.readline
n,m = map(int,input().split())

arr = []
for i in range(n):
    arr.append(list(map(int,input().split(' '))))

conv=[]
for j in range(m):
    x,y = map(int,input().split())
    conv.append((x,y))
    #arr[x-1][y-1] = 2

base = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            base.append((i+1,j+1))
            break

        
res = []
for i in range(m):
    res.append(i +1 + abs(conv[i][0]-base[i][0]) + abs(conv[i][1]-base[i][1]))

print(max(res))