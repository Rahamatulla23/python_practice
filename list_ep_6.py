"""write a python program to replace the last element in a list with anther list 
sample date: [1,3,5,7,9,10][2,4,6]"""
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.pop()
print(a+b)