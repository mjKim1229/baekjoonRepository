import sys 
input = sys.stdin.readline


gradeInNumber = dict({'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0})

totalSubjectWeight = 0
gradeSum = 0  
for _ in range(20): 
    subjectName, subjectWeight , subjectGrade = input().rstrip().split()
    subjectWeight = float(subjectWeight)
    if subjectGrade == 'P': 
        continue
    else:
        totalSubjectWeight += subjectWeight
        gradeSum += (subjectWeight * gradeInNumber[subjectGrade])

print(round(gradeSum/totalSubjectWeight,6))


