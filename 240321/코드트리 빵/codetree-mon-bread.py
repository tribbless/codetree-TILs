import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
board =[]
for _ in range(n):
    board.append(list(map(int,input().split())))

people = [(-1,-1) for _ in range(m+1)]
visited = [[0]*n for _ in range(n)]
step = [[0]*n for _ in range(n)]
conv = [(-1,-1)]
lock = [[0]*n for _ in range(n)]

for _ in range(m):
    cy, cx = map(int,input().split())
    conv.append((cy-1,cx-1))

def isAllPassed():
    for i in range(1,m+1):
        if people[i]!=conv[i]:
            return False
    return True

d=[(-1,0),(0,-1),(0,1),(1,0)]

def bfs(sy, sx):
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0
            step[i][j] = 0
    q = deque()
    q.append((sy,sx))
    visited[sy][sx] = 1
    while q:
        y,x = q.popleft()
            
        for dy,dx in d:
            Y = y + dy
            X = x + dx
            if 0 <= Y < n and 0<= X < n and not visited[Y][X] and lock[Y][X] ==0:
                step[Y][X] = step[y][x]+1
                visited[Y][X] =1
                q.append((Y,X))

def lock_board():
    for i in range(1,m+1):
        if people[i] == conv[i]:
            py,px = people[i]
            lock[py][px] =1

def enterBaseCamp(time):
    global m,n,d,board,people
    cy,cx = conv[time]
    bfs(cy,cx) #편의점이 출발점일 때 step,visited의 경로
    dist = 1e9
    by, bx = -1,-1
    for i in range(n):
        for j in range(n):
            if visited[i][j] and board[i][j]==1 and dist > step[i][j]:
                dist = step[i][j]
                by, bx = i, j

    people[time] = (by,bx)
    lock[by][bx] = 1

def simulate():
    for i in range(1,m+1):
        if people[i] == (-1,-1) or conv[i] == people[i] :
            continue
        cy, cx = conv[i]
        bfs(cy,cx)
        py, px = people[i]
        dist = 1e9
        ty ,tx =-1, -1
        for dy, dx in d:
            PY = py + dy
            PX = px + dx
            if 0 <= PY < n and 0 <= PX < n and visited[PY][PX] and dist > step[PY][PX]:
                dist = step[PY][PX]
                ty, tx = PY, PX

        people[i] = (ty, tx)
    lock_board()
    if time >m:
        return
    enterBaseCamp(time)
time =0
while 1:
    time +=1 
    simulate()
    if isAllPassed():
        break
print(time)