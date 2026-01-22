# write a python program to remove duplicate from a list
ls=list(map(int,input().split()))
ans=[]
for i in ls:
    if i not in ans:
        ans.append(i)
print(ans)