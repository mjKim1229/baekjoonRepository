import sys 
input = sys.stdin.readline 

student = []
n = int(input().rstrip())
for _ in range(n):
    name, lang, eng, math = input().rstrip().split()
    student.append((name,int(lang),int(eng),int(math)))

student.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))

for i in student:
    print(i[0])