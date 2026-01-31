"""Largest of Three Numbers
Input 3 numbers
Find the largest (don’t use max() first time)"""
#num=list(map(int,input("enter numbers: ").split()))
num=list(map(int,input("enter a number ").split(" ")))
max_num = num[0]
for i in num:
    if i > max_num:
        max_num = i
print(max_num)
