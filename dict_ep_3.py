x={}
n=int(input("how many elements "))
for i in range(n):
    k=input("Enter a key: ")
    v=int(input("Enter the value:"))
    x.update({k:v})
print("The dictionary is:",x)