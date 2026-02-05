#write a python program to find revers a number
num=int(input("ENTER A NUMBER: "))
rev=0
while num>00:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print("the reversed number is:",rev)