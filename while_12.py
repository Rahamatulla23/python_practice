#write a python program to display fibinocci series
terms=int(input("Enter no of terms: "))
i=0
num1,num2=1,0
print(num1,num2,end=" ")
while i<=terms-2:
    num3=num1+num2
    print(num3,end="\n")
    num1=num2
    num2=num3
    i+=1
