#write a python program to check number is armstrong number or not
num=int(input("ENTER A NUMBER: "))
backup=num
count=len(str(num))
sum=0
while num>0:
    rem=num%10
    sum+=rem**count
    num=num//10
if backup==sum:
    print("armstrong number")
else:
    print("not a armstrong number")