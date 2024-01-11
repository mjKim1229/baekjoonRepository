import sys 
input = sys.stdin.readline 

def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input().rstrip())

parent = [0] * (n+1)
for i in range(1,n+1):
    parent[i] = i 

edges = []
for i in range(n):
    row = list(map(int,input().rstrip().split())) 
    for j in range(n):
        if i!=j: 
            edges.append((row[j],i+1,j+1))

edges.sort()

result = 0 
for edge in edges:
    dist, a, b = edge 
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += dist 

print(result)