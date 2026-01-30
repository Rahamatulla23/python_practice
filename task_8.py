num =5
counter=0
for x in range(0, num):
    for y in range(0,x+1):
        print(counter, end=" ")
        counter = 2**(x + 1)
    print()