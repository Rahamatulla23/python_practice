#4) Write a Python program to reverse a string without using builtin functions.(frequenly asked question)
s = input("Enter a String: ")
ans = ''

for ch in s:# p,y,t,h,o,n
    ans = ch + ans 

print(ans)