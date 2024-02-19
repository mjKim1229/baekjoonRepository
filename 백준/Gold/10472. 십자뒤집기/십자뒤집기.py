from collections import deque
import copy 

def toString(graph):
    tmpStr = ''
    for i in range(3):
        tmpStr += ''.join(graph[i])

    return tmpStr

dx = [0,1,0,-1]
dy = [1,0,-1,0]


def singleClick(x,y,new_tmp):
    #내자리 
    if new_tmp[x][y] == '*':
        new_tmp[x][y] = '.'
    else: 
        new_tmp[x][y] = '*'
    
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<= xx <3 and 0<= yy <3:
            if new_tmp[xx][yy] == '*':
                new_tmp[xx][yy] = '.'
            else: 
                new_tmp[xx][yy] = '*'

t = int(input().rstrip())
for _ in range(t):
    target = [list(input().rstrip()) for _ in range(3)]
    
    #초기 처리 
    q = deque()
    visited = set()

    #모두 흰색 
    allWhite = [['.'] * 3 for _ in range(3)]
    q.append((allWhite,0))
    visited.add(toString(allWhite))

    while q:
        tmp, time = q.popleft()
        if tmp == target:
            print(time)
            break
    
        #3 X 3 순회 
        for x in range(3):
            for y in range(3):
                new_tmp = copy.deepcopy(tmp)
                singleClick(x,y,new_tmp)
                new_tmp_str = toString(new_tmp)
                if new_tmp_str not in visited:
                    visited.add(new_tmp_str)
                    q.append((new_tmp,time+1))
        


