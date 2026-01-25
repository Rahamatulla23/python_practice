"""write a python program to convert a list of multiple integres into  SINLE INTERER
sample example:[11,22,50]
out:11335"""
l=list(map(int,input().split()))
ans=''
for i in l:
    ans=ans+str(i)
print(ans)