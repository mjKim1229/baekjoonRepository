naturalNum = set(range(1,10001))
generatedNum = set()

for i in range(1,10001): 
    for j in str(i): 
        i += int(j)
    generatedNum.add(i)

selfNumber = sorted(naturalNum-generatedNum)

for i in selfNumber:
    print(i)
