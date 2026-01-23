# write a python program to get the frequency of the elements in a list
ls=list(map(int,input().split()))
ans=dict()
for i in ls:
    count=0
    for ele in ls:
        if i == ele:
            count+=1
    ans[i]=count
print(ans)     