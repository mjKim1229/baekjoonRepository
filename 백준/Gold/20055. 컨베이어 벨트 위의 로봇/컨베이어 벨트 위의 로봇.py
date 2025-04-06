import sys 
input = sys.stdin.readline 
from collections import deque 

N, K = map(int, input().rstrip().split())
belt = deque(map(int, input().rstrip().split()))
robot = deque([0] * N) 
answer = 0 

def new_robot_on():
    if belt[0] != 0 and robot[0] != 1: 
        robot[0] = 1 
        belt[0] -= 1 

while True:
    answer += 1 

    belt.rotate(1)
    robot[-1] = 0 
    robot.rotate(1)
    robot[-1] = 0 

    #어짜피 로봇은 N-1에서 내린다. 
    for i in range(N-2, -1, -1):
        if belt[i+1] >= 1 and robot[i+1] == 0 and robot[i] == 1:
            robot[i+1] = 1 
            robot[i] = 0 
            belt[i+1] -= 1 

    robot[-1] = 0

    new_robot_on()
    if belt.count(0) >= K: 
        break

print(answer)

