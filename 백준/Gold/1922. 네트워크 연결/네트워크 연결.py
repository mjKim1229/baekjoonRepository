import sys 
input = sys.stdin.readline 

def find_parent(parent,x):
    if parent[x] != x: 
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b: 
        parent[b] = a
    else: 
        parent[a] = b 

n = int(input().rstrip())
m = int(input().rstrip())

parent = [0] * (n+1)
for i in range(1,n+1):
    parent[i] = i 

edges = []

for _ in range(m):
    a, b, c = map(int,input().rstrip().split())
    edges.append((c,a,b))

edges.sort()

result = 0 
for edge in edges:
    c, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += c
print(result)


