n, m, k = map(int, input().split())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

directions = list(map(int, input().split()))

# index, 냄새
smell = [[[0, 0]] * n for _ in range(n)]

#상어 index (0~3) : 방향 (0~3) : i (0~3)
priorities = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, input().rstrip().split())))

#무조건 -1 접근
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def in_area(x , y):
    if 0<= x < n and 0<= y <n:
        return True
    return False

def update_smell():
    # 각 위치를 하나씩 확인하며
    for i in range(n):
        for j in range(n):
            # 냄새가 존재하는 경우, 시간을 1만큼 감소시키기
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            # 상어가 존재하는 해당 위치의 냄새를 k로 설정
            if array[i][j] != 0:
                smell[i][j] = [array[i][j], k]

def move():
    new_array = [[0] * n for _ in range(n)]

    #상어 찾기
    for x in range(n):
        for y in range(n):
            #상어면
            if array[x][y] != 0:
                #현재 상어 index (1~4)
                now_shark_index = array[x][y]
                #방향 (1~4)
                direction = directions[now_shark_index-1]
                found = False
                for index in range(4):
                    nx = x + dx[priorities[now_shark_index - 1][direction - 1][index] - 1]
                    ny = y + dy[priorities[now_shark_index - 1][direction - 1][index] - 1]
                    if in_area(nx, ny):
                        #지금 상태에 smell이 없으면 어떻게든 감 -> 방향 바꿈 (밀어내든 새로 들어가든)
                        if smell[nx][ny][1] == 0:
                            #방향 전환
                            directions[now_shark_index-1] = priorities[now_shark_index-1][direction-1][index]

                            if new_array[nx][ny] == 0:
                                new_array[nx][ny] = array[x][y]
                            # 밀어냄 발생 (이전 상어 이동 예정)
                            else:
                                new_array[nx][ny] = min(new_array[nx][ny], array[x][y])
                            found = True
                            break

                if found:
                    continue

                for index in range(4):
                    now_shark_index = array[x][y]
                    nx = x + dx[priorities[now_shark_index - 1][direction - 1][index] - 1]
                    ny = y + dy[priorities[now_shark_index - 1][direction - 1][index] - 1]
                    if in_area(nx, ny):
                        #내 냄새
                        if smell[nx][ny][0] == now_shark_index:
                            directions[now_shark_index - 1] = priorities[now_shark_index - 1][direction - 1][index]
                            new_array[nx][ny] = now_shark_index
                            break
    return new_array


time = 0
while True:
    update_smell() # 모든 위치의 냄새를 업데이트
    new_array = move() # 모든 상어를 이동시키기
    array = new_array # 맵 업데이트
    time += 1 # 시간 증가

    # 1번 상어만 남았는지 체크
    check = True
    for i in range(n):
        for j in range(n):
            if array[i][j] > 1:
                check = False
    if check:
        print(time)
        break

    # 1000초가 지날 때까지 끝나지 않았다면
    if time >= 1000:
        print(-1)
        break
