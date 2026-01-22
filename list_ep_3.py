#write apyhton program to get the largest number from a list
ls=list(map(int,input().split()))
max=0
for i in ls:
    if i>max:
        max=i
print(max)