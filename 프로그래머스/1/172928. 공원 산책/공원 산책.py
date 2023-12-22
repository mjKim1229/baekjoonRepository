def solution(park, routes):
    # 동 남 서 북
    destinationX = [0, 1, 0, -1]
    destinationY = [1, 0, -1, 0]
    destination = ["E", "S", "W", "N"]
    row, column = len(park), len(park[0])
    
    x, y = 0, 0
    
    for i in range(row):
        for j in range(column):
            if park[i][j] == "S":
                x = i
                y = j
                break

                
    for route in routes:
        obstacleFound = False
        dest, go = route.split()
        go = int(go)
        destIndex = destination.index(dest)
        tempX = x + (go * destinationX[destIndex])
        tempY = y + (go * destinationY[destIndex])
       
        if 0 <= tempX < row and 0 <= tempY < column:
            # 경로에 장애물이 있는지 확인
            if dest == "E":
                for i in range(y, tempY + 1):
                    if park[x][i] == "X":
                        obstacleFound = True
            elif dest == "S":
                for i in range(x, tempX + 1):
                    if park[i][y] == "X":
                        obstacleFound = True
            elif dest == "W":
                for i in range(tempY, y + 1):
                    if park[x][i] == "X":
                        obstacleFound = True
            elif dest == "N":
                for i in range(tempX, x + 1):
                    if park[i][y] == "X":
                        obstacleFound = True
        else:
            print("ture")
            obstacleFound = True

        if not obstacleFound:
            x, y = tempX, tempY
    

    # 최종 위치를 반환
    return [x, y]
