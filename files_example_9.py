import sys, os
name = input("Enter File Name: ")

if os.path.isfile(name):
    f = open('naveen.txt', 'r')
else:
    print(name,"file doesn't exists")
    sys.exit()

cl = cw = cc = ca = ua = la = cd = spch = 0
for line in f:
    cc += len(line.rstrip('\n'))
    cw += len(line.split())
    cl += 1
    for ch in line.strip('\n'):
        if ch.isalpha():
            ca += 1
            if ch.isupper():
                ua += 1
            else:
                la += 1
        elif ch.isdigit():
            cd += 1
        else:
            spch += 1

print("No of Lines: ",cl)
print("No of Words: ",cw)
print("No of Characters: ",cc)
print("No of Alphabets: ",ca)
print("No of Uppercase Alphabets: ",ua)
print("No of Lowercase Alphabets: ",la)
print("No of Digits: ",cd)
print("No of Special Characters: ",spch)
