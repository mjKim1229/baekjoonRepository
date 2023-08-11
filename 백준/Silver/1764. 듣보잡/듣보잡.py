import sys 
input = sys.stdin.readline 

n, m = map(int,input().rstrip().split())

setA = set()
setB = set()

for _ in range(n): 
    setA.add(input().rstrip())

for _ in range(m):
    setB.add(input().rstrip() )

#print(setA,setB)
setC = setA & setB 


result = list(setC)
result.sort()
print(len(result))
for i in result: 
    print(i)
