# write a python program to find no of digits in a given number
num=int(input("ENTER A NUMBER: "))
count=0
while num>0:
    num=num//10
    count+=1
print(f"the counts{count}")