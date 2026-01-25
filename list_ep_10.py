#write a python program to find the consist of at least one common  element
ls1=list(map(int,input().split()))
ls2=list(map(int,input().split()))
ans=[]
for i in ls1:
    if i in ls2:
        ans.append(i)
print(ans)