import sys 
input = sys.stdin.readline 
import math 
from itertools import combinations 

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

parent = [0] * n 
for i in range(n):
    parent[i] = i 


location = []
for i in range(n):
    x, y = map(float,input().rstrip().split())
    location.append((i,x,y))

edges = []
for a, b in combinations(location,2):
    xGap = b[2] - a[2]
    yGap = b[1] - a[1]
    distance = round(math.sqrt(xGap * xGap + yGap * yGap) ,2)
    edges.append((distance,a[0],b[0]))

edges.sort()


result = 0 
for edge in edges:
    dist, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += dist

print(result)



