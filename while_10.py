#write a python program to check number is palindrome
num=int(input("Enter a number: "))
backup=num
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
if backup==rev:
    print("THIS IS PALINDROME NUMBER")
else:
    print("THIS IS NOT A PALINDROME NUMBER")
