#write a python program to insert a given string at the beginning of all item in a list
#sample list: [1,2,3,4]string (emp)
#OUT PUT :[emp1,emp2,emp3,emp4]
ls=list(map(int,input().split()))
s=input()
print([f"{s}{i}"for i in ls])
    