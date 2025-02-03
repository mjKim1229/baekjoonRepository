import sys 
input = sys.stdin.readline 

N = int(input().rstrip())

villages = []
people_count = 0
for _ in range(N):
    loc, person = map(int, input().rstrip().split())
    villages.append((loc, person))
    people_count += person

villages.sort(key=lambda x: x[0])

people_now_count = 0
for loc, person in villages:
    people_now_count += person
    if people_now_count >= (people_count /2): 
        print(loc)
        exit(0) 


