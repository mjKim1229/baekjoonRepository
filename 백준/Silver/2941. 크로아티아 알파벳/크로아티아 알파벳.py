import sys 
input = sys.stdin.readline

croatiaAlpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']

target = input().rstrip()

for i in range(len(croatiaAlpha)):
    #print(croatiaAlpha[i],str(i)+str(i))
    target = target.replace(croatiaAlpha[i],str(i))

#print(target)
print(len(target))