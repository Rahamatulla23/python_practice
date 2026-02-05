#write a python program to check weathe strong numnber or not
import math
num=int(input("Enter a Number: "))
backup=num
sum=0
while num>0:
    rem=num%10
    sum=sum+math.factorial(rem)
    num=num//10
if backup==sum:
    print("Strong number")
else:
    print("not a strong num:")