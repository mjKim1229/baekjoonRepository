import sys 
input = sys.stdin.readline 

#0~10 
def dfs(player, sum):
    global answer
    if player == 11:
        answer = max(answer, sum)
        return 
    for position in range(11):
        if graph[player][position] != 0 and not visited[position]:
            visited[position] = True 
            dfs(player +1, sum + graph[player][position]) 
            visited[position] = False 

for _ in range(int(input().rstrip())):
    graph = []
    for _ in range(11):
        row = list(map(int, input().rstrip().split())) 
        graph.append(row) 
    visited = [False] * 11
    answer = 0 
    dfs(0, 0)
    print(answer)