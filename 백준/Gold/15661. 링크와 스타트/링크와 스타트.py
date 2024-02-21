#총 N명 
#스타트 / 링크 팀 
# 1명이상!!!!!
#번호 1~N
#S(ij), S(ji) : i, j 같은 팀일때 팀에 더해지는 능력치 
#sij, sji 다름 
import sys 
input = sys.stdin.readline 
from itertools import combinations

#전체 사람 수 : n 
n = int(input().rstrip())

#점수 표 
scores = [ list(map(int, input().rstrip().split())) for _ in range(n)]

#모든 좌표 
totalLoc = set(x for x in range(n)) 

firstTeamCombi = []
#팀 구성 
def makeFirstTeam(teamNum):
    for team in combinations(totalLoc,teamNum):
        firstTeamCombi.append(team)

#한팀당 2개씩 뽑아서 값 더해주기 
def singleTeamSum(team):
    teamSum = 0 
    for x,y in combinations(team,2):
        teamSum += scores[x][y]
        teamSum += scores[y][x]
    return teamSum

#첫 번째 팀원 수 (1~n//2)
for i in range(1,(n//2)+1):
    makeFirstTeam(i)

answer = int(1e9)
#한 팀마다 2개씩 뽑아 계산 
for firsTeam in firstTeamCombi:
    fSum, sSum = 0,0 
    if len(firsTeam) >= 2:
        fSum = singleTeamSum(firsTeam)

    
    #남은 팀은 secondTeam 
    secondTeam = totalLoc - set(firsTeam)
    if len(secondTeam) >= 2: 
        sSum = singleTeamSum(secondTeam)
    
    
    gap = abs(fSum-sSum)
    answer = min(answer,gap)
    
print(answer)
    


