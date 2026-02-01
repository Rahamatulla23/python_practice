x={}
n=int(input("how many players: "))
for i in range(n):
    k=input("Enter player name: ")
    v=int(input("Enter runs: "))
    x.update({k:v})
print("\n player in match: ")
for pname in x.keys():
    print(pname)
name=input("Enter player name: ")
runs=x.get(name,-1)
if(runs ==-1):
    print("players not found ")
else:
    print(f"{name}mand runs {runs}")