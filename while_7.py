#write a python program to find sum of digits in a given number
num=int(input("enter a number: "))
s=0
while num>0:
    rem=num%10
    s=s+rem
    num=num//10
print("sum of digits s:",s)