start = int(input("Enter starting Number: "))
stop = int(input("Enter starting Number: "))
count  = 0
for num in range(start,stop+1):
    if num>1:
        for i in range(2,num):
            if num%i ==0:
                break
        else:
            print(num,end='\t')
            count += 1

print("\nNo of Primes =",count)