import sys
input = sys.stdin.readline

start, end, stream = input().rstrip().split()
inSet = set()
outSet = set()
while True:
    try:
        time, name = input().rstrip().split()
        if time<=start and name not in inSet: 
            inSet.add(name)
        elif end <= time <=stream and name not in outSet: 
            outSet.add(name)
    except: 
        break

print(len(inSet & outSet))