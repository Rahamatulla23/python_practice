#write a python program to multiplay all thr items in a list
ls=list(map(int,input().split()))
ans=1
for i in ls:
    ans*=i
print(ans)