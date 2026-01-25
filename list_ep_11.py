"""write a python prgram to remove consective duplicates of a given list
original list:[0,0,1,2,3,4,4,5,6,6,6,7,8,9,4,4 ] 
after removing consecitve duplicates:[0,1,2,3,4,5,6,7,8,9,4]"""
ls=list(map(int,input().split(",")))
ans=[]
prev=None
for i in ls:
    if i!=prev:
        ans.append(i)
        prev=i
print(ans)