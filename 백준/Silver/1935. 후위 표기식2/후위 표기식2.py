import sys 
input = sys.stdin.readline 
from collections import deque 

N = int(input().rstrip()) 
total_array = list(input().rstrip())
num_array = deque()
stack = []
for _ in range(N): 
    num_array.append(int(input().rstrip())) 

def calculate(data, num1, num2): 
    if data == '+':
        return num1 + num2
    if data == '-':
        return num1 - num2
    if data == '*':
        return num1 * num2 
    if data == '/':
        return num1 / num2

for data in total_array:
    if data.isalpha():
        stack.append(num_array[ord(data)-65])
    else: 
        num1 = stack.pop()
        num2 = stack.pop()
        result = calculate(data, num2, num1)
        stack.append(result)
        
print('%.2f' %stack[-1])

