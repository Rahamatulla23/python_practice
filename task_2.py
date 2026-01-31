"""Positive / Negative / Zero
Input a number
Identify its type"""
num=int(input("enter a number: "))
if num>0:
    print(num,"is a positive number")
elif num<0:
    print(num,"is a negative number")
else:
    print(num,"is a not positive or negative number")